import uuid

from fastapi import APIRouter, Depends, status

from app.dependencies import get_task_service
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskRead])
async def list_tasks(service: TaskService = Depends(get_task_service)):
    return await service.get_all()


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(data: TaskCreate, service: TaskService = Depends(get_task_service)):
    return await service.create(data)


@router.patch("/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: uuid.UUID, data: TaskUpdate, service: TaskService = Depends(get_task_service)
):
    return await service.update(task_id, data)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: uuid.UUID, service: TaskService = Depends(get_task_service)):
    await service.delete(task_id)
