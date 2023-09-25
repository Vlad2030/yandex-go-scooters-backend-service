from config.data import App
from core.database import Base, engine
from core.middleware.cors import setup_cors_middleware
from fastapi import FastAPI
from routers.api_routes import router
from utils.logging import logger, set_basic_logger


def create_application() -> FastAPI:
    application = FastAPI(
        title=App.TITLE,
        version=App.VERSION,
        docs_url=App.DOCS_URL,
        redoc_url=None,
    )
    setup_cors_middleware(app=application)
    set_basic_logger()
    application.include_router(router=router)

    @application.on_event("startup")
    async def startup() -> None:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        return logger.info("Application startup")

    @application.on_event("shutdown")
    async def shutdown() -> None:
        return logger.warning("Application shutdown")

    return application


app = create_application()
