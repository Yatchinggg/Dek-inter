from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import select
from . import database, models

app = FastAPI()


class StartRequest(BaseModel):
    nickname: str


@app.on_event("startup")
async def startup():
    await database.init_db()


@app.post("/start")
async def start_quiz(req: StartRequest):

    async with database.AsyncSessionLocal() as session:

        result = await session.execute(
            select(models.NicknameCount).where(
                models.NicknameCount.nickname == req.nickname
            )
        )

        record = result.scalar_one_or_none()

        if record:
            record.count += 1
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
