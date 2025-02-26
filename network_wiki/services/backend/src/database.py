from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(
    "postgresql+asyncpg://admin:admin@postgres:5432/networks_db", echo=True
)
async_session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
