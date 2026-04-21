from typing import Final
from decouple import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool
    db_url: str
    api_prefix: str
    maintenance_prefix: str


SETTINGS: Final[Settings] = Settings(
    debug=config("DEBUG"),
    db_url=config("DB_URL"),
    api_prefix="/api",
    maintenance_prefix="/maintenance"
)
