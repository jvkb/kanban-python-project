import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Query, status

from app.dependencies import get_task_service
from app.schemas.task import Status, TaskCreate, TaskListResponse, TaskRead, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=TaskListResponse)
async def list_tasks(
    status_filter: Annotated[Status | None, Query(alias="status")] = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 50,
    offset: Annotated[int, Query(ge=0)] = 0,
    service: TaskService = Depends(get_task_service),
):
    return await service.get_all(status=status_filter, limit=limit, offset=offset)


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
