# pip install ollama
import ollama
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': "Define 'supervised learning' in simple terms? Give me one sentance answer",
  },
])
print("AI: ",response['message']['content'])


# Links 1: https://github.com/ollama/ollama
# Links 2: https://github.com/ollama/ollama-python