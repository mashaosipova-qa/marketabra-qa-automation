from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BASE_URL_API: str = ""
    ENVIRONMENT: str = ""
    EMAIL_SELLER: str = ""
    PASSWORD_SELLER: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()


