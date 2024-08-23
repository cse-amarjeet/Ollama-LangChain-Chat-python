import ollama

stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': 'What color is the sky on a clear day? Give me one sentance answer'}],
    stream=True,  #set stream True
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

print()  # New line