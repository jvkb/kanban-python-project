from fastapi import Depends
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.redis_client import redis
from app.repositories.task_repository import TaskRepository
from app.services.ai_service import AIService
from app.services.task_service import TaskService


async def get_task_repository(session: AsyncSession = Depends(get_db)) -> TaskRepository:
    return TaskRepository(session)


async def get_task_service(
    repository: TaskRepository = Depends(get_task_repository),
) -> TaskService:
    return TaskService(repository)


async def get_redis() -> Redis:
    return redis


async def get_ai_service(redis: Redis = Depends(get_redis)) -> AIService:
    return AIService(redis)
