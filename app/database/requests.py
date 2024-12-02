from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select, update, delete

async def set_user(tg_id, age, experience, level, goal, type_tr, quantity, zones):

    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, age=age,
                             experience=experience, level=level,
                             goal=goal, type_tr=type_tr,
                             quantity=quantity, zones=zones))
            await session.commit()

async def get_info(tg_id):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))
