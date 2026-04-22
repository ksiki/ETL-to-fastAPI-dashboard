from typing import Annotated, Final

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db_helper import DATABASE_HELPER
from src.api.v1.crud import sales_crud as crud
from src.api.v1.schemas.sales_schemas import SalesFilters


ROUTER: Final[APIRouter] = APIRouter()


@ROUTER.get("/")
async def get_sales(
    filters: Annotated[SalesFilters, Query()],
    session: AsyncSession = Depends(DATABASE_HELPER.session_dependency)
):
    return await crud.get_sales(
        session=session, 
        filters=filters
    )
