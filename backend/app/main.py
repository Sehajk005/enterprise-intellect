"""App factory, middleware, routers. Fully populated in phase 1; ping lives here for 0.4."""

from fastapi import FastAPI

from app.api.v1.ping import router as ping_router


def create_app() -> FastAPI:
    app = FastAPI(title="Enterprise Intellect")
    app.include_router(ping_router, prefix="/api/v1")
    return app


app = create_app()
