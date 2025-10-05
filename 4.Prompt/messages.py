from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)