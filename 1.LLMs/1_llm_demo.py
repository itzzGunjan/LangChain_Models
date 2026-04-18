from langchain_openai import OpenAI
from dotenv import load_dotenv               #import dotenv


load_dotenv()

llm = OpenAI(model='gpt-4o-mini') # we can put any model inside this comma

result = llm.invoke("What is the rich thing about dhanbad") #llm  takes string as input and string as output 

print(result)