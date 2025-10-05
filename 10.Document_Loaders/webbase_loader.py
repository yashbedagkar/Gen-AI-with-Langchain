from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.in/Lenovo-i5-13450HX-300Nits-Graphics-83DV00BHIN/dp/B0CX8V9C7D?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A2HOAOQSENRDV8'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser 

print(chain.invoke({'question':"What is the summary of all the reviews?",'text':docs[0].page_content}))

# returns 1 document object per url