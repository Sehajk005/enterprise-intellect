# Enterprise Intellect V2

## Setup

1. Clone the repo.
2. Copy `.env.example` to `.env` and fill in the two required keys — `GEMINI_API_KEY` (Google AI Studio) and `PINECONE_API_KEY` (Pinecone). Every other variable already has a working default for local development.
3. Install backend dependencies (Python 3.12, managed with [uv](https://docs.astral.sh/uv/)):
   ```
   cd backend
   uv sync --locked
   ```
4. Install frontend dependencies (Node 20/22):
   ```
   cd frontend
   npm ci
   ```
5. Install the pre-commit hooks (see Developer tooling below).

The full stack (Postgres, backend, frontend via `docker compose up`) lands in phase 0.4 — steps 3-4 above are enough to have both projects installed and ready today.

## Toolchain versions

| Tool                     | Required       | Installed on this machine       |
| ------------------------ | -------------- | ------------------------------- |
| Python                   | 3.12           | 3.12.6 (`.python-version`)      |
| Node.js                  | 20 or 22 (LTS) | 22.14.0 (`.nvmrc`)              |
| Docker Desktop / Compose | Compose v2     | Docker 29.1.3 / Compose v2.40.3 |
| Git                      | —              | 2.51.0                          |

Verify with:

```
python --version
node --version
docker compose version
git --version
```

## Developer tooling

Pre-commit hooks (Ruff lint+format, mypy, ESLint, Prettier, detect-secrets scan) are configured in `.pre-commit-config.yaml`. After cloning:

```
pip install pre-commit detect-secrets
pre-commit install
```

Editor settings are in `.editorconfig`.
