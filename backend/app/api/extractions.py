from fastapi import APIRouter, HTTPException

from backend.app.schemas.extraction import ExtractionResult
from backend.app.services.extractions import ExtractionStore

router = APIRouter(prefix="/files", tags=["extractions"])


@router.get("/{file_id}/extraction", response_model=ExtractionResult)
def get_extraction(file_id: str) -> ExtractionResult:
    store = ExtractionStore()
    result = store.get(file_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Extraction not found")
    return result


@router.post("/{file_id}/extraction", response_model=ExtractionResult)
def upsert_extraction(file_id: str, payload: ExtractionResult) -> ExtractionResult:
    if payload.file_id != file_id:
        raise HTTPException(status_code=400, detail="file_id mismatch")
    store = ExtractionStore()
    return store.save(payload)
