from fastapi import APIRouter
from app.api.v1.endpoints.main_trigger.model import TriggerResponse

router = APIRouter()

@router.get("/trigger", response_model=TriggerResponse)
async def main_trigger():
    try:
        return TriggerResponse(
            result="Trigger principal executado com sucesso!"
        )
    except Exception as e:
        print("Erro no trigger principal:", e)
        return TriggerResponse(result="Erro ao executar o trigger principal.")