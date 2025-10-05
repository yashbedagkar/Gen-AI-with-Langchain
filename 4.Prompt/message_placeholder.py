# A MessagesPlaceholder in LangChain is a special placeholder used inside a 
# ChatPromptTemplate to dynamically insert chat history or a list of messages at runtime

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system','You are a helpful assistant'),
    MessagesPlaceholder(variable_name ='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('4.Prompt/chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history) 

prompt = chat_template.invoke({'chat_history':chat_history,'query':'Where is my refund?'})

print(prompt)

# import os
# print("Current Working Directory:", os.getcwd())
