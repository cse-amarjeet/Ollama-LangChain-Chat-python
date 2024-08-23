from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Create a ChatOllama model
model = ChatOllama(model="llama3")

# Define prompt templates with a computer science theme
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert in computer science. Answer questions with short, concise answers."),
        ("human", "Explain the difference between a stack and a queue in one sentence."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser() # StrOutputParser will remove the irrelevant information.

# Run the chain
result = chain.invoke({})

# Output the result
print("\nAI: ",result)
