from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})

result = parallel_chain.invoke({'topic':'Rise of AI'})

# print(result['tweet'])
# print(result['linkedin'])

print(result)