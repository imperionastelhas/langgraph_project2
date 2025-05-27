from fastapi import APIRouter
from app.api.v1.endpoints.main_trigger.model import TriggerResponse, MessageInput
from app.core.agent.graph import graph

router = APIRouter()

@router.post("/invoke", response_model=TriggerResponse)
async def main_trigger(input: MessageInput):
    try:
        result = await graph.ainvoke({"messages": input.messages}) 
        last_msg = result["messages"][-1].content
        return TriggerResponse(result=last_msg)
    except Exception as e:
        print("Erro no trigger principal:", e)
        return TriggerResponse(result="Erro ao executar o trigger principal.")