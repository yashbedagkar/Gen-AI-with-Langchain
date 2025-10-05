from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
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

prompt1 = template1.invoke({'topic':'Black hole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result1.content})

result2 = model.invoke(prompt2)

print(result2.content)