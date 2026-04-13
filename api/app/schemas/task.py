import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel

Status = Literal["todo", "in_progress", "done"]
Priority = Literal["low", "medium", "high"]


class TaskListResponse(BaseModel):
    items: list["TaskRead"]
    total: int
    limit: int
    offset: int


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: Status = "todo"
    priority: Priority = "medium"
    category: str | None = None
    estimated_minutes: int | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: Status | None = None
    priority: Priority | None = None
    category: str | None = None
    estimated_minutes: int | None = None


class TaskRead(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None
    status: Status
    priority: Priority
    category: str | None
    estimated_minutes: int | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
