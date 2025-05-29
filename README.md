# Projeto Langgraph API

## How to build
```
python -m venv [project-name]

cd [project-name]

git clone [git-link]

cd [git-name]

pip install -r requirements.txt
```

## Structure
langgraph_project/
├── app/
│   ├── __init__.py
│   ├── api/                  # Rotas FastAPI
│   │   └── routes.py
│   ├── core/                 # Núcleo do sistema (LangGraph + config)
│   │   ├── langflow/         # Fluxo e lógica do LangGraph
│   │   │   ├── __init__.py
│   │   │   ├── graph.py      # Define o fluxo LangGraph
│   │   │   ├── nodes.py      # Nós (funções, agentes, ferramentas etc.)
│   │   │   └── classifier.py # (opcional) Classificador para múltiplos fluxos
│   │   ├── config.py         # Configurações do projeto
│   │   └── logger.py         # Logger padrão
│   ├── services/             # Lógica externa (integração, banco, etc.)
│   │   └── conversation.py
│   ├── models/               # Pydantic/SQLModel schemas
│   │   └── schema.py
│   └── main.py               # Inicializa o FastAPI
├── .env
├── requirements.txt
├── README.md
└── tests/
    └── test_flow.py


## Message json
{
  "event": "messages.upsert",
  "instance": "Carlos Gabriel",
  "data": {
    "key": {
      "remoteJid": "558888651157@s.whatsapp.net",
      "fromMe": false,
      "id": "C2B62AED6DAFD01851D54558C7877024"
    },
    "pushName": "Jus Digital",
    "status": "DELIVERY_ACK",
    "message": {
      "conversation": "Opa",
      "messageContextInfo": {
        "deviceListMetadata": {
          "senderKeyHash": "B1OHm3rWim2czg==",
          "senderTimestamp": "1748288682",
          "recipientKeyHash": "eLIbkyL+wkdnXQ==",
          "recipientTimestamp": "1748517126"
        },
        "deviceListMetadataVersion": 2,
        "messageSecret": "IMDT2IP97MXvk6Tx/C8ZFe5f/Jsttg1FvuFWLQGWHJY="
      }
    },
    "messageType": "conversation",
    "messageTimestamp": 1748517690,
    "instanceId": "90eba6d9-83e6-4eb6-a2f1-3ef7be8dfe46",
    "source": "android"
  },
  "destination": "https://8362-187-19-149-59.ngrok-free.app/api/v1/trigger/invoke",
  "date_time": "2025-05-29T08:21:31.086Z",
  "sender": "558781713642@s.whatsapp.net",
  "server_url": "https://evolution-evolution.u7npqi.easypanel.host",
  "apikey": "A7CFA28E347B-42EA-9F5C-D8DFD7FE78A7"
}

## Audio message json:
{
  "event": "messages.upsert",
  "instance": "Carlos Gabriel",
  "data": {
    "key": {
      "remoteJid": "558888651157@s.whatsapp.net",
      "fromMe": false,
      "id": "8C58EE20A1B1583F93224ABD2ECDCFE2"
    },
    "pushName": "Jus Digital",
    "status": "DELIVERY_ACK",
    "message": {
      "audioMessage": {
        "url": "https://mmg.whatsapp.net/v/t62.7117-24/30024350_550453338133643_1166916748197930861_n.enc?ccb=11-4&oh=01_Q5Aa1gFhHaXbtiz_n79SUjrxdNqz7h17hUrqSrR1g9pZ096ecg&oe=685FD0A7&_nc_sid=5e03e0&mms3=true",
        "mimetype": "audio/ogg; codecs=opus",
        "fileSha256": "eEoFTXjN4rKLksmID5N87teDtkQhEWR+MbxnSH9Xq+o=",
        "fileLength": "4409",
        "seconds": 2,
        "ptt": true,
        "mediaKey": "fvu8QV8J+2CRGxLezt3BOSyujXp7gedMVHVyjDglEAE=",
        "fileEncSha256": "KxLATGMVW3wrRpI+JedS7WiIBKvjn2bX9JFNdRB3qz0=",
        "directPath": "/v/t62.7117-24/30024350_550453338133643_1166916748197930861_n.enc?ccb=11-4&oh=01_Q5Aa1gFhHaXbtiz_n79SUjrxdNqz7h17hUrqSrR1g9pZ096ecg&oe=685FD0A7&_nc_sid=5e03e0",
        "mediaKeyTimestamp": "1748518341",
        "waveform": "AAAAAAUNFxkaGh4eGhkaHBcUFB4hISEdGBUaIBwcHBgXGR4eHR8dGhocHRodHx4eICIgHRodHx8jIx4cHB8fHw=="
      },
      "messageContextInfo": {
        "deviceListMetadata": {
          "senderKeyHash": "B1OHm3rWim2czg==",
          "senderTimestamp": "1748288682",
          "recipientKeyHash": "eLIbkyL+wkdnXQ==",
          "recipientTimestamp": "1748517126"
        },
        "deviceListMetadataVersion": 2,
        "messageSecret": "I+3mgljrtyd/6nuC4lIZcjzHM5Yg0yWhwNW/G+e02eo="
      }
    },
    "contextInfo": null,
    "messageType": "audioMessage",
    "messageTimestamp": 1748518341,
    "instanceId": "90eba6d9-83e6-4eb6-a2f1-3ef7be8dfe46",
    "source": "android"
  },
  "destination": "https://8362-187-19-149-59.ngrok-free.app/api/v1/trigger/invoke",
  "date_time": "2025-05-29T08:32:21.688Z",
  "sender": "558781713642@s.whatsapp.net",
  "server_url": "https://evolution-evolution.u7npqi.easypanel.host",
  "apikey": "A7CFA28E347B-42EA-9F5C-D8DFD7FE78A7"
}

## Image message json:

{
  "event": "messages.upsert",
  "instance": "Carlos Gabriel",
  "data": {
    "key": {
      "remoteJid": "558888651157@s.whatsapp.net",
      "fromMe": false,
      "id": "718EFA24FCEEEB30DD3438C23EBF22AB"
    },
    "pushName": "Jus Digital",
    "status": "DELIVERY_ACK",
    "message": {
      "imageMessage": {
        "url": "https://mmg.whatsapp.net/v/t62.7118-24/25432630_870830358576687_2346514322414021550_n.enc?ccb=11-4&oh=01_Q5Aa1gFpcIXqUo4LUk66U1LknLlnDlys9MX4bZWruhRxEGiwrQ&oe=685FA9ED&_nc_sid=5e03e0&mms3=true",
        "mimetype": "image/jpeg",
        "fileSha256": "Y7oiWbAZDWzGFLL7UItwVySV2IGUmYYABK87ufX22tA=",
        "fileLength": "45579",
        "height": 1103,
        "width": 540,
        "mediaKey": "iUO6XAxjwtZRaQOrPtEgPYUSDdXchR6kzW9KK8Dsqf0=",
        "fileEncSha256": "LZxhCz2kRiL546YuEhJV5p9Njp8ru4/QqX34DjsmqeE=",
        "directPath": "/v/t62.7118-24/25432630_870830358576687_2346514322414021550_n.enc?ccb=11-4&oh=01_Q5Aa1gFpcIXqUo4LUk66U1LknLlnDlys9MX4bZWruhRxEGiwrQ&oe=685FA9ED&_nc_sid=5e03e0",
        "mediaKeyTimestamp": "1748518590",
        "jpegThumbnail": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEABsbGxscGx4hIR4qLSgtKj04MzM4PV1CR0JHQl2NWGdYWGdYjX2Xe3N7l33gsJycsOD/2c7Z//////////////8BGxsbGxwbHiEhHiotKC0qPTgzMzg9XUJHQkdCXY1YZ1hYZ1iNfZd7c3uXfeCwnJyw4P/Zztn////////////////CABEIAEUAIQMBIgACEQEDEQH/xAAuAAADAQEBAAAAAAAAAAAAAAAAAwQCBQEBAQEBAQAAAAAAAAAAAAAAAAABAgP/2gAMAwEAAhADEAAAAET9HObBq7NRlYdRNUInGURSIF6nCsl1FHUVmxFJBjfnTLPVZsaJD0BcehYAH//EACQQAAIBAwQCAgMAAAAAAAAAAAABAgMREgQUIVETMUFSMlNh/9oACAEBAAE/AJQNtDo20Ojb0/qben9SULCgYDiYk6dzxE6ijXw+Mbm603zI3Wl+4ypq4JtIk6NSp5JPmw9Pp7m20/Rq6/jjivchO902cmT7M32TreV3nD0Vl6srGnjTjSxn8k9NSl+M7G0j+wlLo4lJXFMyTOBWsWRwxo5ExmXtCk2Zfw//xAAaEQACAwEBAAAAAAAAAAAAAAAAAQIREhAg/9oACAECAQE/AOukaiaiSMsyxq16/8QAGxEAAgEFAAAAAAAAAAAAAAAAAAERAhASICH/2gAIAQMBAT8AuiGYspJJFzb/2Q==",
        "scansSidecar": "xHenQexN2lXiTtgdYQhTPQTzgmLfvKYOgfIGQMRhaTsneKQH895DjA==",
        "scanLengths": [
          5512,
          13242,
          9034,
          17791
        ],
        "midQualityFileSha256": "QQCrwYIuZ9aKVxf7pfFfz+D86S/Nt8E+iQnTdcFOPQk="
      },
      "messageContextInfo": {
        "deviceListMetadata": {
          "senderKeyHash": "B1OHm3rWim2czg==",
          "senderTimestamp": "1748288682",
          "recipientKeyHash": "eLIbkyL+wkdnXQ==",
          "recipientTimestamp": "1748517126"
        },
        "deviceListMetadataVersion": 2,
        "messageSecret": "01VUGsnrBtPLTVkRWI9dELDFSPrWXMBX5Sf/3xIOXPM="
      }
    },
    "contextInfo": null,
    "messageType": "imageMessage",
    "messageTimestamp": 1748518593,
    "instanceId": "90eba6d9-83e6-4eb6-a2f1-3ef7be8dfe46",
    "source": "android"
  },
  "destination": "https://8362-187-19-149-59.ngrok-free.app/api/v1/trigger/invoke",
  "date_time": "2025-05-29T08:36:33.436Z",
  "sender": "558781713642@s.whatsapp.net",
  "server_url": "https://evolution-evolution.u7npqi.easypanel.host",
  "apikey": "A7CFA28E347B-42EA-9F5C-D8DFD7FE78A7"
}

## Sticker message json:

{
  "event": "messages.upsert",
  "instance": "Carlos Gabriel",
  "data": {
    "key": {
      "remoteJid": "558888651157@s.whatsapp.net",
      "fromMe": false,
      "id": "0EEEA14EAD9FBAB6B7D0725C01DFA753"
    },
    "pushName": "Jus Digital",
    "status": "DELIVERY_ACK",
    "message": {
      "stickerMessage": {
        "url": "https://mmg.whatsapp.net/v/t62.15575-24/19740465_1043158183948679_497990251588054944_n.enc?ccb=11-4&oh=01_Q5Aa1gFQSF96tVG2LRfEFy8GKByZB2Fp4Dp6owa-CQ-DziGE8g&oe=685FCD57&_nc_sid=5e03e0&mms3=true",
        "fileSha256": "nSuZJERpTLVb6B4cgeY4lRTVqS70Vw6P7B02M6pYVPc=",
        "fileEncSha256": "eMtkEjn0wwWvC59NKfreDkumFBNWeSt6CxCBcfABNlg=",
        "mediaKey": "LBzsX8UcpxYQPVuHIhEbsFNWIvreZGvBjuKtjQPhj70=",
        "mimetype": "image/webp",
        "height": 512,
        "width": 512,
        "directPath": "/v/t62.15575-24/19740465_1043158183948679_497990251588054944_n.enc?ccb=11-4&oh=01_Q5Aa1gFQSF96tVG2LRfEFy8GKByZB2Fp4Dp6owa-CQ-DziGE8g&oe=685FCD57&_nc_sid=5e03e0",
        "fileLength": "11268",
        "mediaKeyTimestamp": "1748519333",
        "isAnimated": false,
        "stickerSentTs": "1748519333943",
        "isAvatar": false,
        "isAiSticker": false,
        "isLottie": false
      },
      "messageContextInfo": {
        "deviceListMetadata": {
          "senderKeyHash": "B1OHm3rWim2czg==",
          "senderTimestamp": "1748288682",
          "recipientKeyHash": "eLIbkyL+wkdnXQ==",
          "recipientTimestamp": "1748517126"
        },
        "deviceListMetadataVersion": 2,
        "messageSecret": "VA7eb5q6mkH+O8AxoOa0RdYTUxZ0evR+C8fsxn3R65A="
      }
    },
    "contextInfo": null,
    "messageType": "stickerMessage",
    "messageTimestamp": 1748519334,
    "instanceId": "90eba6d9-83e6-4eb6-a2f1-3ef7be8dfe46",
    "source": "android"
  },
  "destination": "https://8362-187-19-149-59.ngrok-free.app/api/v1/trigger/invoke",
  "date_time": "2025-05-29T08:48:54.640Z",
  "sender": "558781713642@s.whatsapp.net",
  "server_url": "https://evolution-evolution.u7npqi.easypanel.host",
  "apikey": "A7CFA28E347B-42EA-9F5C-D8DFD7FE78A7"
}

## Document message:

{
  "event": "messages.upsert",
  "instance": "Carlos Gabriel",
  "data": {
    "key": {
      "remoteJid": "558888651157@s.whatsapp.net",
      "fromMe": false,
      "id": "B49FAC32B078CF40B2500BBCC65CBF0E"
    },
    "pushName": "Jus Digital",
    "status": "DELIVERY_ACK",
    "message": {
      "documentMessage": {
        "url": "https://mmg.whatsapp.net/v/t62.7119-24/30907959_2869223149932624_4264599815158238449_n.enc?ccb=11-4&oh=01_Q5Aa1gHIp-jvo5dKwlTyMo2MNrMqETHIzZQXMX4p3I1sFUzXxA&oe=685FBA50&_nc_sid=5e03e0&mms3=true",
        "mimetype": "application/pdf",
        "fileSha256": "F7z9/G0DpCII3TdhVrJUiese8CmKe5MLM1K2H6HJRNI=",
        "fileLength": "82243",
        "pageCount": 3,
        "mediaKey": "5NqeCy+wFZAdXRYZc2Inq19WnuoJMGGwSEsF2YfFdBA=",
        "fileName": "formulario_jus_digital.pdf",
        "fileEncSha256": "ZjeBUTIR5JFQfJriOne3YLUfBF7xNcRNiUnL+fOQeLs=",
        "directPath": "/v/t62.7119-24/30907959_2869223149932624_4264599815158238449_n.enc?ccb=11-4&oh=01_Q5Aa1gHIp-jvo5dKwlTyMo2MNrMqETHIzZQXMX4p3I1sFUzXxA&oe=685FBA50&_nc_sid=5e03e0",
        "mediaKeyTimestamp": "1748519436",
        "thumbnailDirectPath": "/v/t62.36145-24/21603591_1043471950636299_592012948488081832_n.enc?ccb=11-4&oh=01_Q5Aa1gFj9XI9O-hNzwoySOqmx9-0O4NXoeFuYwG_BW6sl4JdRg&oe=685FB19A&_nc_sid=5e03e0",
        "thumbnailSha256": "RqF0rK7jYnKlPdpgAlaTcnkSL85Kkz82h8NBR3SwNSM=",
        "thumbnailEncSha256": "clEFNxZPqbIEnJITSElnMXirjWXK/VnjrqPNPvrQYAI=",
        "jpegThumbnail": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEABERERESERMVFRMaHBkcGiYjICAjJjoqLSotKjpYN0A3N0A3WE5fTUhNX06MbmJiboyiiIGIosWwsMX46/j///8BERERERIRExUVExocGRwaJiMgICMmOiotKi0qOlg3QDc3QDdYTl9NSE1fToxuYmJujKKIgYiixbCwxfjr+P/////CABEIAGAASgMBIgACEQEDEQH/xAArAAEBAQEBAQAAAAAAAAAAAAAAAQMCBAYBAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhADEAAAAPvDzHpY6lQVBQMdoYb8DRmNEoA56yOZzoa2CgAZ6cGfXXRHQ56lAGWvJg1hNpQlAHPQ46oigAD/xAAzEAABAwEFBQUHBQAAAAAAAAABAAIRAwQSIVKREyAxYZIUIiRBUTAyU3GCoaJCYnLR4f/aAAgBAQABPwD2daqadSBWc3DgGqi2vXF5tpMAxi1dnr4+IOiFC04zafxXZ7Rj4kj6VsLQQPFHpRZVDmna4eYjcqPax0FpPDzhCq0mAwn6kNlAk/dRSzfdXW89VcHPVXRuPBnBzh8lBzPUHM9XXZ3qDnemEtmS4qeR3KkmpxHTKAd6joWPr+CYaZwLMebVdblCutyhXW+g3KpZtDJA4fqKBZ6t6nJlN1QS0NP1OTLOZ74EcnOTWhvDerEtqRfgIOZx2zlLPjuV0cdsdVcHxzqrkjCq5NYQZvuO4+pUY4hrRoV2q0ZG6FMtFSSXt0BW2blfots3K/RAyJ3apu1D7vlxJUxk6z/Skfs63Ki518XBTJ/m47721L3dD45EK5WmIqahXa2IipqEx1RogsceZIV9/wAI6jefSrF3dIj5wjZ7VmHX/iaK9McGnmSga0iQzUoT7f8A/8QAFBEBAAAAAAAAAAAAAAAAAAAAQP/aAAgBAgEBPwB3/8QAFBEBAAAAAAAAAAAAAAAAAAAAQP/aAAgBAwEBPwB3/9k=",
        "thumbnailHeight": 480,
        "thumbnailWidth": 370
      },
      "messageContextInfo": {
        "deviceListMetadata": {
          "senderKeyHash": "B1OHm3rWim2czg==",
          "senderTimestamp": "1748288682",
          "recipientKeyHash": "eLIbkyL+wkdnXQ==",
          "recipientTimestamp": "1748517126"
        },
        "deviceListMetadataVersion": 2,
        "messageSecret": "xlPS8wK5rD1mbZPFQPiJWoYr3B9zb+KwIYU/i3r3ue4="
      }
    },
    "contextInfo": null,
    "messageType": "documentMessage",
    "messageTimestamp": 1748519437,
    "instanceId": "90eba6d9-83e6-4eb6-a2f1-3ef7be8dfe46",
    "source": "android"
  },
  "destination": "https://8362-187-19-149-59.ngrok-free.app/api/v1/trigger/invoke",
  "date_time": "2025-05-29T08:50:38.093Z",
  "sender": "558781713642@s.whatsapp.net",
  "server_url": "https://evolution-evolution.u7npqi.easypanel.host",
  "apikey": "A7CFA28E347B-42EA-9F5C-D8DFD7FE78A7"
}

## From me message:

{
  "event": "messages.upsert",
  "instance": "Carlos Gabriel",
  "data": {
    "key": {
      "remoteJid": "558888651157@s.whatsapp.net",
      "fromMe": true,
      "id": "7EE94D10DA26C8870F638651DC0FA0BA"
    },
    "pushName": "Carlos Gabriel",
    "status": "SERVER_ACK",
    "message": {
      "messageContextInfo": {
        "messageSecret": "X57MRkCBIjGAb0howncy9wTPhBIm2Zh0xnyiKe7GQxs="
      },
      "conversation": "Opa"
    },
    "contextInfo": {
      "entryPointConversionSource": "global_search_new_chat",
      "entryPointConversionApp": "whatsapp",
      "entryPointConversionDelaySeconds": 79652
    },
    "messageType": "conversation",
    "messageTimestamp": 1748519596,
    "instanceId": "90eba6d9-83e6-4eb6-a2f1-3ef7be8dfe46",
    "source": "android"
  },
  "destination": "https://8362-187-19-149-59.ngrok-free.app/api/v1/trigger/invoke",
  "date_time": "2025-05-29T08:53:17.073Z",
  "sender": "558781713642@s.whatsapp.net",
  "server_url": "https://evolution-evolution.u7npqi.easypanel.host",
  "apikey": "A7CFA28E347B-42EA-9F5C-D8DFD7FE78A7"
}