from __future__ import annotations

from dotenv import load_dotenv
import os
from dataclasses import dataclass
from typing import Any, Dict, List, TypedDict

from langchain_core.runnables import RunnableConfig
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph
from langgraph.prebuilt import create_react_agent

# --- Carrega a chave da OpenAI (assumindo que está no .env) ---
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

# --- Ferramenta de exemplo ---
async def get_weather(city: str) -> str:
    """Return a simple weather report for the given city."""
    return f"It's always sunny in {city}!"

# --- Configuração dinâmica (opcional) ---
class Configuration(TypedDict):
    prompt: str

# --- Estrutura do estado que trafega entre os nós ---
@dataclass
class State:
    messages: List[BaseMessage]

# --- Define o agente com ferramentas e prompt ---
agent = create_react_agent(
    model="openai:gpt-4o-mini",
    tools=[get_weather],
    prompt="You are a helpful assistant",
)

# --- Nó principal que executa o agente ---
async def call_model(state: State, config: RunnableConfig) -> Dict[str, Any]:
    output = await agent.ainvoke({"messages": state.messages}, config=config)
    return {"messages": output["messages"]}

# --- Construção e exportação do grafo ---
graph = (
    StateGraph(State, config_schema=Configuration)
    .add_node(call_model)
    .add_edge("__start__", "call_model")
    .compile(name="agent")
)

graph.get_graph().name = "agent"
