from fastapi import APIRouter
from app.api.v1.endpoints.main_trigger import main_trigger

router = APIRouter()
router.include_router(main_trigger.router, prefix="/trigger", tags=["invoke main trigger"])