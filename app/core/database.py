from config.data import Database
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (f"postgresql+asyncpg://"
                f"{Database.USER}:{Database.PASSWORD}"
                f"@{Database.HOST}:{Database.PORT}/"
                f"{Database.DB}")
Base = declarative_base()
metadata = MetaData()
engine = create_async_engine(url=DATABASE_URL, echo=False)
async_session = sessionmaker(engine,
                             expire_on_commit=False, class_=AsyncSession)


def create_all(engine: AsyncEngine) -> None:
    return metadata.create_all(engine)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session
