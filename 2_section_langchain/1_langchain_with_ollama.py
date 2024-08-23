# pip install -qU langchain-ollama langchain  (update the packages)
# Link: https://python.langchain.com/v0.2/docs/integrations/chat/ollama/

from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

llm = ChatOllama(
    model="llama3",
    temperature=0.9)

messages = [
    (
        "system",
        "You are a helpful assistant that help user to answer the query. Answer the query in one sentance",
    ),
    ("human", "What is machine learning definition?"),
]
ai_msg = llm.invoke(messages)
print("AI: ",ai_msg.content)