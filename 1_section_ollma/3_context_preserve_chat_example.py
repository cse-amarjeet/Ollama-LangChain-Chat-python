import ollama

# Initialize an empty list to store chat history
chat_history = []

while True:
    user_message = input("You: ")

    # types 'exit' to end the chat
    if user_message.lower() == 'exit':
        print("Exiting the chat.")
        break

    chat_history.append({'role': 'user', 'content': user_message}) # Append the user query
    response = ollama.chat(model='llama3', messages=chat_history)  #Generate the answer 
    chat_history.append({'role': 'assistant', 'content': response['message']['content']})  # Append the generated answer to the chat history

    # print the generated answer
    print("AI: ", response['message']['content'])
