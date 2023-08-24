from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


MongoConfig = MongoSettings()
