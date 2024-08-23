import ollama

# Store history
chat_history = []

while True:
    # User message
    user_message = input("You: ")

    # Type 'exit' to Exit the chat
    if user_message.lower() == 'exit':
        print("Exiting the chat.")
        break

    # Append the user's message to the chat history
    chat_history.append({'role': 'user', 'content': user_message})

    # Send the chat history to the model with streaming enabled
    stream = ollama.chat(
        model='llama3',
        messages=chat_history,
        stream=True  # Enable streaming
    )

    # Capture the streamed response
    assistant_response = ""
    for chunk in stream:
        content = chunk['message']['content']
        assistant_response += content
        print(content, end='', flush=True)
    
    print()  # For a newline after the streamed response

    # Append the assistant's response to the chat history
    chat_history.append({'role': 'assistant', 'content': assistant_response})
 