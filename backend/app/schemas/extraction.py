from __future__ import annotations

from pydantic import BaseModel, Field

from backend.app.schemas.geometry import BoundingBox, Hole


class ExtractionResult(BaseModel):
    file_id: str
    file_type: str
    confidence_score: float | None = None
    bounding_box: BoundingBox | None = None
    volume: float | None = None
    surface_area: float | None = None
    holes: list[Hole] = Field(default_factory=list)
    complexity_score: float | None = None
    warnings: list[str] = Field(default_factory=list)
