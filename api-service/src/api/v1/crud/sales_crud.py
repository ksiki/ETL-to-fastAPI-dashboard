from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1.schemas.sales_schemas import SalesFilters, Sales
from src.models.models import (
    CalendarORM, 
    SalesORM,
    ProductORM
)


async def get_sales(session: AsyncSession, filters: SalesFilters) -> list[Sales]:
    stmt = (
        select(
            CalendarORM.fact_date.label("date"),
            SalesORM.hour,
            ProductORM.name.label("prod_name"),
            SalesORM.total_sales,
            SalesORM.count_sales_with_sub,
            SalesORM.count_sales_without_sub,
            SalesORM.count_refunded,
            SalesORM.total_revenue
        )
        .join(CalendarORM, CalendarORM.id == SalesORM.date_id)
        .join(ProductORM, ProductORM.str_id == SalesORM.prod_id)
    )

    if filters.start_date:
        stmt = stmt.where(CalendarORM.fact_date >= filters.start_date)
    if filters.end_date:
        stmt = stmt.where(CalendarORM.fact_date <= filters.end_date)
    
    result: Result = await session.execute(stmt)
    sales = result.mappings().all()
    return [Sales.model_validate(sale) for sale in sales]
