import pytest
from sqlalchemy import text

pytestmark = pytest.mark.integration


async def test_throwaway_database_is_usable(db_engine, test_database_name):
    async with db_engine.connect() as conn:
        current = (await conn.execute(text("select current_database()"))).scalar_one()
        assert current == test_database_name
        assert (await conn.execute(text("select 1"))).scalar_one() == 1
    assert test_database_name.startswith("test_ei_")
