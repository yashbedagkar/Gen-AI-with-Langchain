from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

#promt1
template1 = PromptTemplate(
    template='Write the detailed report on {topic}',
    input_variables=['topic']
) 

#promt2
template2 = PromptTemplate(
    template='Write the 5 lines summary of the following text {text}',
    input_variables=['text']
) 

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

# StrOutputParser extracts the content fron the result and returns it in a string format
# It is helpful when working with chains