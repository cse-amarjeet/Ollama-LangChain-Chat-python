from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate

# Create a ChatOllama model with llama3
model = ChatOllama(model="llama3",temperature=0.9)

# # PART 1: Template string
# template = "what is {topic}. give me one sentance answer"
# prompt_template = ChatPromptTemplate.from_template(template)

# prompt = prompt_template.invoke({"topic": "deep learning"})
# result = model.invoke(prompt)
# print("\nQuery: ",prompt)
# print("\n\nAI: ",result.content)

# PART 2: Multiple Placeholders
# template_multiple = """You are a helpful assistant.
# Human: Tell me a story on {topic} in {length}.
# Assistant:"""
# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"topic": "cat", "length": "one sentance"})
# print("\nQuery: ",prompt)  # print the query
# result = model.invoke(prompt)
# print("\n\nAI: ",result.content)

# # PART 3: Prompt with System and Human Messages (Using Tuples)
# messages = [
#     ("system", "You are a expert of {topic}. give me one word answer"),
#     ("human", "when {event}."),
# ]
# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic": "history", "event": "India got freedom"})
# print("\nQuery: ",prompt)  # print the query
# result = model.invoke(prompt)
# print("\n\nAI: ",result.content)
