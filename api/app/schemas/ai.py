from pydantic import BaseModel

from app.schemas.task import Priority


class AIAnalyzeRequest(BaseModel):
    title: str
    description: str | None = None


class AIAnalyzeResponse(BaseModel):
    priority: Priority
    category: str
    estimated_minutes: int
    reasoning: str
