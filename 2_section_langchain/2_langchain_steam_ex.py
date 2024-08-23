from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

# Initialize the ChatOllama model with streaming enabled
llm = ChatOllama(
    model="llama3",
    temperature=0.9,
    stream=True  # Enable streaming
)
# Define the messages
messages = [
    (
        "system",
        "You are a helpful assistant that helps the user answer the query. Answer the query in one sentence.",
    ),
    ("human", "What is machine learning definition?"),
]

# Invoke the model with streaming
ai_msg_stream = llm.stream(messages)

# Capture and print the streamed response
full_response = ""
for chunk in ai_msg_stream:
    content = chunk.content
    full_response += content
    print(content, end='', flush=True)

print()  # Print a newline

