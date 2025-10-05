from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'), # pass a tuple in ChatPromptTemplate
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)

# dynamic single query (single turn interaction) --> PromptTemplate
# dynamic multiple query (multi turn interaction) --> ChatPromptTemplate