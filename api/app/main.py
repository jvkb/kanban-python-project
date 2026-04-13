from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

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


@v1.get("/health")
async def health():
    return {"status": "ok"}
