import logging
from typing import Final

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src import maintenance
from src.core.config import SETTINGS 
from src.api.v1.api import API_ROUTER as api_v1


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOG: Final[logging.Logger] = logging.getLogger(__name__)

app = FastAPI()


app.state.is_maintenance = False
@app.middleware("http")
async def maintenance_check(request: Request, call_next):
    if app.state.is_maintenance and SETTINGS.maintenance_prefix not in request.url.path:
        if request.url.path.startswith(SETTINGS.api_prefix):
            return JSONResponse(
                status_code=503,
                content={
                    "status": "maintenance",
                    "message": "System is under maintenance (DB Vacuuming). Please wait.",
                },
                headers={"Retry-After": "300"} 
            )
    response = await call_next(request)
    return response


app.include_router(maintenance.ROUTER, prefix=SETTINGS.maintenance_prefix, tags=["System"])
app.include_router(api_v1, prefix=SETTINGS.api_prefix)
