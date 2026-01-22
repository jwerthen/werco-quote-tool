from datetime import datetime

from pydantic import BaseModel


class FileUploadResponse(BaseModel):
    file_id: str
    filename: str
    status: str


class FileRecordResponse(BaseModel):
    file_id: str
    filename: str
    status: str
    storage_path: str
    created_at: datetime
