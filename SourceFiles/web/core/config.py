from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv('.env')


class Settings(BaseSettings):
    DB_USER: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int


settings = Settings()
