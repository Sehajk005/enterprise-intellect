"""Shared fixtures.

- ``client``: async HTTP client bound to the app in-process (no server needed).
- ``database_url`` / ``test_database_name`` / ``db_engine``: a throwaway Postgres
  database created once per test session on the Compose ``db`` service and dropped
  at the end. If Postgres is unreachable, tests that use it are skipped with a hint.
- Fake providers live in ``tests/fakes`` (filled in 2.1.5).
"""

import asyncio
import os
import uuid
from collections.abc import AsyncIterator, Iterator

import asyncpg
import httpx
import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from app.main import create_app

# Admin connection (to the default "postgres" database) used only to create/drop test DBs.
# Defaults match docker-compose.yml's db service published on localhost:5434.
# pragma: allowlist nextline secret
_DEFAULT_DSN = "postgresql://postgres:postgres@localhost:5434/postgres"
ADMIN_DSN = os.environ.get("TEST_DATABASE_ADMIN_DSN", _DEFAULT_DSN)


async def _admin_execute(statement: str) -> None:
    conn = await asyncpg.connect(ADMIN_DSN, timeout=5)
    try:
        await conn.execute(statement)
    finally:
        await conn.close()


@pytest.fixture
async def client() -> AsyncIterator[httpx.AsyncClient]:
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        yield c


@pytest.fixture(scope="session")
def test_database_name() -> Iterator[str]:
    name = f"test_ei_{uuid.uuid4().hex[:12]}"
    try:
        asyncio.run(_admin_execute(f'CREATE DATABASE "{name}"'))
    except (OSError, asyncpg.PostgresError, TimeoutError) as exc:
        pytest.skip(f"Postgres not reachable ({exc!r}); run `docker compose up -d db`")
    yield name
    asyncio.run(_admin_execute(f'DROP DATABASE IF EXISTS "{name}" WITH (FORCE)'))


@pytest.fixture(scope="session")
def database_url(test_database_name: str) -> str:
    base = ADMIN_DSN.rsplit("/", 1)[0]
    return base.replace("postgresql://", "postgresql+asyncpg://", 1) + f"/{test_database_name}"


@pytest.fixture
async def db_engine(database_url: str) -> AsyncIterator[AsyncEngine]:
    engine = create_async_engine(database_url)
    try:
        yield engine
    finally:
        await engine.dispose()
