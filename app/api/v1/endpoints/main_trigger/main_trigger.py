from fastapi import APIRouter
from app.api.v1.endpoints.main_trigger.model import TriggerResponse, WebhookRequestList
from app.core.agent.graph import graph

router = APIRouter()

@router.post("/invoke", response_model=TriggerResponse)
async def main_trigger(client_id: str, payload: WebhookRequestList):
    try:
        # result = await graph.ainvoke({"messages": input.messages}) 
        # last_msg = result["messages"][-1].content
        for event in payload.__root__:
            msg = event.body.data.message.conversation
            sender = event.body.sender
            print(f"Mensagem de {sender} para {client_id}: {msg}")
        return TriggerResponse(result="last_msg")
    except Exception as e:
        print("Erro no trigger principal:", e)
        return TriggerResponse(result="Erro ao executar o trigger principal.")