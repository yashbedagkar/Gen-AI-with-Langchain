# when we use a document loader, in return we get a list of document objects
# every document object contains page_content and metadata

from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

prompt = PromptTemplate(
    template='Write a summary on the following poem \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('10.Document_Loaders/cricket.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))