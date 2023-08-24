from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router
from core.config.app import AppConfig


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def init_cors(app_: FastAPI) -> None:
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=AppConfig.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app() -> FastAPI:
    # init app
    app_ = FastAPI(
        title=AppConfig.APP_NAME,
        description=AppConfig.APP_Description,
        version=AppConfig.APP_VERSION,
        docs_url=None if AppConfig.ENVIRONMENT == "production" else "/docs",
        redoc_url=None,
    )
    init_routers(app_=app_)
    init_cors(app_=app_)
    return app_


app = create_app()
