from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

# Initialize the ChatOllama model with streaming enabled
llm = ChatOllama(
    model="llama3",
    temperature=0.9,
    stream=True  # Enable streaming
)

# Initialize an empty list to store chat history
chat_history = [
    ("system", "You are a helpful assistant that helps the user answer the query. Answer the query in one sentence.")
]

# Start a loop for continuous interaction
while True:
    # Get the user's message input
    user_message = input("You: ")

    # Exit the loop if the user types 'exit'
    if user_message.lower() == 'exit':
        print("Exiting the chat.")
        break

    # Append the user's message to the chat history
    chat_history.append(("human", user_message))

    # Invoke the model with streaming enabled
    ai_msg_stream = llm.stream(chat_history)

    # Capture and print the streamed response
    full_response = ""
    for chunk in ai_msg_stream:
        content = chunk.content
        full_response += content
        print(content, end='', flush=True)

    print("\n\n")  # Print a newline after the streaming finishes

    # Append the assistant's response to the chat history
    chat_history.append(("assistant", full_response))
