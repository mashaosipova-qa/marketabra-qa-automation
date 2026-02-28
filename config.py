from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

#DataBase settings
class DBConfig(BaseModel):
    name: str
    user: str
    password: str
    host: str
    port: int

#Seller credentials
class SellerConfig(BaseModel):
    email: str = ""
    password: str = ""

#Aggregates sub-configs (DB, Seller, API)
class Settings(BaseSettings):
    base_url_api: str = ""
    environment: str = ""

    #Nested Data Models
    db: DBConfig
    seller: SellerConfig

    model_config=SettingsConfigDict(env_file=".env", env_nested_delimiter="__", extra="ignore")

settings = Settings()





