from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.app.schemas.files import FileRecordResponse, FileUploadResponse
from backend.app.services.files import FileRepository
from backend.app.services.storage import LocalFileStorage

router = APIRouter(prefix="/files", tags=["files"])


@router.post("/upload", response_model=FileUploadResponse)
def upload_file(file: UploadFile = File(...)) -> FileUploadResponse:
    storage = LocalFileStorage()
    file_id, path = storage.save(file)
    FileRepository().create(
        file_id=file_id,
        filename=file.filename,
        status="queued",
        storage_path=path,
    )
    return FileUploadResponse(file_id=file_id, filename=file.filename, status="queued")


@router.get("/{file_id}", response_model=FileRecordResponse)
def get_file(file_id: str) -> FileRecordResponse:
    record = FileRepository().get(file_id)
    if record is None:
        raise HTTPException(status_code=404, detail="File not found")
    return FileRecordResponse(
        file_id=record.file_id,
        filename=record.filename,
        status=record.status,
        storage_path=str(record.storage_path),
        created_at=record.created_at,
    )
