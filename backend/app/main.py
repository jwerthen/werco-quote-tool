from fastapi import FastAPI

from backend.app.api.router import router


def create_app() -> FastAPI:
    app = FastAPI(title="QuoteEngine API", version="0.1.0")
    app.include_router(router)
    return app


app = create_app()
