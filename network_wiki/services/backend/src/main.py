from fastapi import FastAPI
from database import engine, Base, async_session_maker
from models import USOFiber, USOL2VPN
import manuals, network_hardware_config_files, uso
from contextlib import asynccontextmanager


async def fill_database():
    """
    Создает все таблицы
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def seed_data():
    """
    Подключается к сессии и заполняет таблицы первичными данными
    """
    async with async_session_maker() as session:
        async with session.begin():
            session.add_all(
                [
                    USOFiber(
                        name_uso="GK-Roscosmos",
                        number_uso=2,
                        type_uso=1,
                        address="Berejkovskaya, 22, korp 1",
                        contact="897768123851",
                    ),
                    USOFiber(
                        name_uso="GK-Roscosmos",
                        number_uso=1,
                        type_uso=1,
                        address="Schepkina, 42",
                        contact="897768123851",
                    ),
                    USOFiber(
                        name_uso="FGUP NTC Zarya",
                        number_uso=32,
                        type_uso=2,
                        address="2-ya Brestskaya, d9, str. 1",
                        contact="897768123851",
                    ),
                    USOL2VPN(
                        name_uso="Bazalt",
                        number_uso=68,
                        type_uso=5,
                        address="Tulskaya obl, Schekinskiy raion, stroitelnaya baza",
                        contact="897768123851",
                    ),
                    USOL2VPN(
                        name_uso="Zlatmasch",
                        number_uso=47,
                        type_uso=5,
                        address="Zlatoust, Parkovii proezd, d.1",
                        contact="897768123851",
                    ),
                    USOL2VPN(
                        name_uso="EHO",
                        number_uso=34,
                        type_uso=7,
                        address="Himki",
                        contact="897768123851",
                    ),
                ]
            )
            await session.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Выполняет предварительные действия перед запуском FastApi
    """
    print("Creating tables...")
    await fill_database()
    print("Seeding data...")
    await seed_data()
    yield
    print("Delete tables...")


app = FastAPI(lifespan=lifespan)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:8080"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
def home():
    """
    Базовый эндпоинт для проверки доступности
    :return: Text
    """
    return "Hello, World!"


app.include_router(manuals.router)
app.include_router(network_hardware_config_files.router)
app.include_router(uso.router)


