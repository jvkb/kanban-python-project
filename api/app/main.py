from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from app.exceptions import TaskNotFoundError
from app.routers import ai, tasks

app = FastAPI(
    title="Kanban AI API",
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:5173"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ],
)

v1 = FastAPI()
app.mount("/v1", v1)

v1.include_router(tasks.router)
v1.include_router(ai.router)


@v1.exception_handler(TaskNotFoundError)
async def task_not_found_handler(request: Request, exc: TaskNotFoundError) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": f"Task {exc.task_id} not found"})


@v1.get("/health")
async def health():
    return {"status": "ok"}
