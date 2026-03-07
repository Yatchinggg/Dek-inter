import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

engine = create_async_engine(DATABASE_URL, echo=False)

Base = declarative_base()

async def init_db():
    # import models here to register them with Base
    from . import models
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
