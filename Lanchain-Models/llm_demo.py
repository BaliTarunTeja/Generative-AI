from langchain_openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from a .env file which contains the OpenAI API key
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')
# Usage of invoke method to get the response from the LLM and invoke function takes prompt as input and returns the response from the LLM
result = llm.invoke("What is the capital of India")

print(result)