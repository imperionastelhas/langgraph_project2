from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api.v1.api_router import router as api_v1_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Inicializando...")
    yield
    print("Finalizando aplicação...")

app = FastAPI(title="Langgraph API", lifespan=lifespan)

origins = [
    "http://localhost:3000",  # por exemplo, se seu frontend estiver em React
    "http://127.0.0.1:3000",
    "https://seu-front-end.com",  # substitua pelo domínio real em produção
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router, prefix="/api/v1")