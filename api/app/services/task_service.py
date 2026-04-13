import uuid

from app.exceptions import TaskNotFoundError
from app.models.task import Task
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    async def get_all(self) -> list[Task]:
        return await self.repository.get_all()

    async def get_by_id(self, task_id: uuid.UUID) -> Task:
        task = await self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError(task_id)
        return task

    async def create(self, data: TaskCreate) -> Task:
        task = Task(**data.model_dump())
        return await self.repository.create(task)

    async def update(self, task_id: uuid.UUID, data: TaskUpdate) -> Task:
        task = await self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError(task_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(task, field, value)
        return await self.repository.update(task)

    async def delete(self, task_id: uuid.UUID) -> None:
        task = await self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError(task_id)
        await self.repository.delete(task)
