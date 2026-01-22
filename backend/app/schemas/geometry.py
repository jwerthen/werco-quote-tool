from __future__ import annotations

from pydantic import BaseModel


class BoundingBox(BaseModel):
    length: float
    width: float
    height: float
    units: str


class Hole(BaseModel):
    diameter: float
    depth: float | None = None
    hole_type: str
    position: tuple[float, float, float] | None = None
