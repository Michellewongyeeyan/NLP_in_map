import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

DEBUG = bool(os.getenv("FASTAPI_DEBUG", True))

app = FastAPI( title="Mongo Fast API", docs_url="/api/docs" if DEBUG else None, redoc_url=None)

origins = [ "*" ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# # Model
from api.chapter.routes import router as ChapterRoutes
app.include_router(ChapterRoutes, tags=["Chapter"], prefix="/api/chapter")

# 測試 API 是否運行中

@app.get("/", tags=["Root"])
async def index():
    return {"message": "Welcome to Alchemist API!"}