import os
from langgraph.prebuilt import create_react_agent

os.environ["OPENAI_API_KEY"] = ""

def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_react_agent(
    model="openai:gpt-4o-mini",
    tools=[get_weather],  
    prompt="You are a helpful assistant"  
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

# Extrai a última mensagem do tipo AIMessage com conteúdo não vazio
final_message = next(
    (msg for msg in reversed(response['messages']) 
     if getattr(msg, 'type', None) == 'ai' and msg.content), 
    None
)

print(final_message.content if final_message else "No final message found.")