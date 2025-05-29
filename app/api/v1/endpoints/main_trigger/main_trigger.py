import httpx
from fastapi import APIRouter
from app.api.v1.endpoints.main_trigger.model import WhatsAppEvent, TriggerResponse

router = APIRouter()

EVOLUTION_API_URL = "https://evolution-evolution.u7npqi.easypanel.host"

@router.post("/invoke", response_model=TriggerResponse)
async def main_trigger(payload: WhatsAppEvent):
    try:
        message = payload.data.message
        CompanyNumber = payload.sender or "desconhecido"
        ClientNumber = payload.data.key.get("remoteJid", "desconhecido")
        ClientName = payload.data.pushName or "desconhecido"
        MessageType = payload.data.messageType or "desconhecido"
        MessageId = payload.data.key.get("id", "desconhecido")
        base64_data = payload.data.message.get("base64", "desconhecido")
        fromMe = payload.data.key.get("fromMe", False)
        isGroup = ClientNumber.endswith("@g.us")
        
        apikey = payload.apikey
        instanceName = payload.instance

        # Detectar tipo de mensagem
        if "conversation" in message:
            content = message["conversation"]
        elif "audioMessage" in message:
            # content = f"Áudio: {message['audioMessage'].get('url', 'sem URL')}"
            base64_data = await get_audio_base64(MessageId, apikey, instanceName)
            content = f"Áudio recebido. Base64: {base64_data[:30]}..."
        elif "imageMessage" in message:
            content = f"Imagem: {message['imageMessage'].get('url', 'sem URL')}"
        elif "documentMessage" in message:
            content = f"Documento: {message['documentMessage'].get('fileName', 'sem nome')}"
        elif "stickerMessage" in message:
            content = "Sticker recebido."
        else:
            content = "Tipo de mensagem não reconhecido."

        print(f"FromMe: {fromMe}, IsGroup: {isGroup}")	
        print(f"CompanyNumber: {CompanyNumber}")
        print(f"ClientNumber: {ClientNumber}, ClientName: {ClientName}")
        print(f"MessageType: {MessageType}, MessageId: {MessageId}")
        print(f"Conteúdo da mensagem: {content}")
        print(f"Base64: {base64_data[:30]}")
        return TriggerResponse(result=content)

    except Exception as e:
        print("Erro no trigger principal:", repr(e))
        return TriggerResponse(result="Erro ao executar o trigger principal.")
    
async def get_audio_base64(message_id: str, api_key: str, instance_name: str) -> str:
    """
    Chama a rota getBase64FromMediaMessage da EvolutionAPI para obter o base64 de uma mensagem de áudio.
    """
    url = f"{EVOLUTION_API_URL}/chat/getBase64FromMediaMessage/{instance_name}"
    headers = {
        "Content-Type": "application/json",
        "apikey": api_key
    }
    payload = {
        "message": {
            "key": {
                "id": message_id
            }
        },
        "convertToMp4": True
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("base64", "base64 não encontrado")
        except httpx.HTTPError as http_err:
            print(f"Erro HTTP ao obter base64: {http_err}")
            return "erro ao obter base64"
        except Exception as err:
            print(f"Erro inesperado ao obter base64: {err}")
            return "erro ao obter base64"

# @router.post("/invoke", response_model=TriggerResponse)
# async def main_trigger(payload):
#     try:
#         # result = await graph.ainvoke({"messages": input.messages}) 
#         # last_msg = result["messages"][-1].content
#         print(payload)
#         for event in payload.__root__:
#             msg = event.body.data.message.conversation
#             sender = event.body.sender
#             print(f"Mensagem de {sender}: {msg}")
#         return TriggerResponse(result="last_msg")
#     except Exception as e:
#         print("Erro no trigger principal:", e)
#         return TriggerResponse(result="Erro ao executar o trigger principal.")