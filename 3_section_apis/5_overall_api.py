import ollama

# #chat with model
response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': 'Why is the sky blue? Give me a very short answer'}])
print(response['message']['content'])

#chat with model easly
# response = ollama.generate(model='llama3', prompt='Why is the sky blue? Give me a very short answer')
# print(response['response'])

# #list
# print("\n List: ")
# print(ollama.list())

# #show
# print(ollama.show('llama3'))


# Create
# modelfile='''
# FROM llama3
# SYSTEM You are mario from super mario bros.
# '''
# ollama.create(model='llama_temp', modelfile=modelfile)


# Delete
# ollama.delete('llama_temp')



# # Embeddings
# print("\n Embeddings: ")
# ollama.embeddings(model='llama3.1', prompt='The sky is blue because of rayleigh scattering')


