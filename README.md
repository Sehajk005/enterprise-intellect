# Enterprise Intellect V2

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

Pre-commit hooks (Ruff lint+format, mypy, ESLint, Prettier, gitleaks secret scan) are configured in `.pre-commit-config.yaml`. After cloning:

```
pip install pre-commit
pre-commit install
```

Editor settings are in `.editorconfig`.
