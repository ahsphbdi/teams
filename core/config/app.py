from pydantic_settings import BaseSettings, SettingsConfigDict

from enum import Enum


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class AppSettings(BaseSettings):
    APP_NAME: str
    APP_Description: str
    APP_VERSION: str
    APP_DEBUG: bool
    BASE_URL: str
    DEFAULT_LOCALE: str
    ENVIRONMENT: str
    Worker: int
    ORIGINS: list[str]
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


AppConfig = AppSettings()
