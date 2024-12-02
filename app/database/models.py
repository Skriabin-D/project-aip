from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id = mapped_column(BigInteger)
    age: Mapped[str] = mapped_column(String)
    experience: Mapped[str] = mapped_column(String(50))
    level: Mapped[str] = mapped_column(String(50))
    goal: Mapped[str] = mapped_column(String(50))
    type_tr: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[str] = mapped_column(String(50))
    #zones: Mapped[str] = mapped_column(String(50))




async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)