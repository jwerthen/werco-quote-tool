from fastapi import APIRouter

from backend.app.api.extractions import router as extractions_router
from backend.app.api.files import router as files_router

router = APIRouter(prefix="/api")


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


router.include_router(files_router)
router.include_router(extractions_router)
