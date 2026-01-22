from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "QuoteEngine API"
    environment: str = "development"
    storage_path: str = "backend/storage"


settings = Settings()
