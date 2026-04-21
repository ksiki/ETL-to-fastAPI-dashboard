from typing import Final

from pydantic_settings import BaseSettings


class Prefixes(BaseSettings):
    version_prefix: str
    users: str
    sales: str


PREFIXES: Final[Prefixes] = Prefixes(
    version_prefix="/v1",
    users="/users",
    sales="/sales"    
)
