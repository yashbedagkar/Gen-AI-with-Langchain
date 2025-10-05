from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic} in short',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

parser = StrOutputParser()

chain = prompt | model | parser

user_input = input(str("Tell a topic : "))

result = chain.invoke({'topic':user_input})

print(result)

chain.get_graph().print_ascii()