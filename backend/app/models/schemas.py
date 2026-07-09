# backend/app/models/schemas.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class StylePrompt(BaseModel):
    id: str
    name: str
    description: str
    prompt: str

class GenerateRequest(BaseModel):
    style: str = "modern"
    num_variations: int = 4

class GenerateResponse(BaseModel):
    success: bool
    images: List[str]
    style: str
    count: int
    generated_at: str

class InspireResponse(BaseModel):
    success: bool
    images: List[str]
    style: str
    count: int

class HealthResponse(BaseModel):
    status: str
    api_key_configured: bool

class ErrorResponse(BaseModel):
    detail: str
    status_code: int
