from pydantic import BaseModel, Field, ConfigDict
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

#Supplier credentials
class SupplierConfig(BaseModel):
    email: str = ""
    password: str = ""

class TestDataConfig(BaseModel):
    default_product_id: int = 1

#Aggregates sub-configs (DB, Seller, API)
class Settings(BaseSettings):
    base_url_api: str = ""
    environment: str = ""

    #Nested Data Models
    db: DBConfig
    seller: SellerConfig
    supplier: SupplierConfig
    test_data: TestDataConfig = TestDataConfig()

    model_config=SettingsConfigDict(env_file=".env", env_nested_delimiter="__", extra="ignore")

settings = Settings()





