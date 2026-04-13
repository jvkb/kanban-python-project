import hashlib

from openai import AsyncOpenAI
from redis.asyncio import Redis

from app.config import settings
from app.constants import AI_CACHE_TTL
from app.prompts import ANALYZE_TASK_SYSTEM
from app.schemas.ai import AIAnalyzeRequest, AIAnalyzeResponse


class AIService:
    def __init__(self, redis: Redis):
        self.redis = redis
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def analyze(self, data: AIAnalyzeRequest) -> AIAnalyzeResponse:
        cache_key = self._cache_key(data)

        cached = await self.redis.get(cache_key)
        if cached:
            return AIAnalyzeResponse.model_validate_json(cached)

        result = await self._call_openai(data)

        await self.redis.setex(cache_key, AI_CACHE_TTL, result.model_dump_json())
        return result

    async def _call_openai(self, data: AIAnalyzeRequest) -> AIAnalyzeResponse:
        user_content = f"Title: {data.title}"
        if data.description:
            user_content += f"\nDescription: {data.description}"

        response = await self.client.chat.completions.parse(
            model="gpt-5",
            response_format=AIAnalyzeResponse,
            messages=[
                {"role": "system", "content": ANALYZE_TASK_SYSTEM},
                {"role": "user", "content": user_content},
            ],
        )

        return response.choices[0].message.parsed

    @staticmethod
    def _cache_key(data: AIAnalyzeRequest) -> str:
        content = f"{data.title}:{data.description or ''}"
        digest = hashlib.sha256(content.encode()).hexdigest()
        return f"ai:{digest}"
