import logging
from typing import Final

from fastapi import FastAPI

from src.user.views import ROUTER 


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOG: Final[logging.Logger] = logging.getLogger(__name__)


app = FastAPI()
app.include_router(ROUTER)
