from typing import Final

from fastapi import APIRouter

from src.api.v1 import users
from src.api.v1 import sales
from src.api.v1.config import PREFIXES


API_ROUTER: Final[APIRouter] = APIRouter(prefix=PREFIXES.version_prefix)

API_ROUTER.include_router(users.ROUTER, prefix=PREFIXES.users, tags=[f"{PREFIXES.version_prefix}{PREFIXES.users}"])
API_ROUTER.include_router(sales.ROUTER, prefix=PREFIXES.sales, tags=[f"{PREFIXES.version_prefix}{PREFIXES.sales}"])
