from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda,RunnableBranch


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

prompt1 = PromptTemplate(
    template = 'Give a report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Summarize this report {report}',
    input_variables=['report']
) 

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1,model,parser)

conditional_chain = RunnableBranch(
    (lambda x: len(x.split())> 300 ,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)  

final_chain = RunnableSequence(report_gen_chain,conditional_chain) 

result = final_chain.invoke({'topic':'Rise of LLMs'})

print(result)