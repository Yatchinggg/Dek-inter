from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import select

from . import models
from . import database

app = FastAPI()

# 允许前端访问（GitHub Pages）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StartRequest(BaseModel):
    nickname: str


@app.on_event("startup")
async def startup():
    await database.init_db()


@app.post("/start")
async def start_quiz(req: StartRequest):
    async with database.AsyncSessionLocal() as session:
        # look up nickname
        result = await session.execute(
            select(models.NicknameCount).where(
                models.NicknameCount.nickname == req.nickname
            )
        )

        record = result.scalar_one_or_none()

        if record:
            record.count += 1
            session.add(record)
        else:
            record = models.NicknameCount(
                nickname=req.nickname,
                count=1
            )
            session.add(record)

        await session.commit()

        return {
            "nickname": record.nickname,
            "count": record.count
        }
