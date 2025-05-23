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