from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Sales(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    date: date
    hour: int
    prod_name: str
    total_sales: int
    count_sales_with_sub: int
    count_sales_without_sub: int
    count_refunded: int
    total_revenue: int


class SalesFilters(BaseModel):
    start_date: Optional[date] = Field(None)
    end_date: Optional[date] = Field(None)
