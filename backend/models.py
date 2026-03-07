from sqlalchemy import Column, Integer, String
from .database import Base


class NicknameCount(Base):
    __tablename__ = "nickname_counts"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, unique=True, index=True, nullable=False)
    count = Column(Integer, default=0)
