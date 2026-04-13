from fastapi import APIRouter, Depends

from app.dependencies import get_ai_service
from app.schemas.ai import AIAnalyzeRequest, AIAnalyzeResponse
from app.services.ai_service import AIService

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/analyze", response_model=AIAnalyzeResponse)
async def analyze_task(data: AIAnalyzeRequest, service: AIService = Depends(get_ai_service)):
    return await service.analyze(data)
