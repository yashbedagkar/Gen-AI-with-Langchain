# What is PydanticOutputParser in LangChain?
# PydanticOutputParser is a structured output parser in LangChain that uses Pydantic models to enforce schema validation when processing LLM responses.

# Why Use PydanticOutputParser?
# Strict Schema Enforcement - Ensures that LLM responses follow a well-defined structure.
# Type Safety - Automatically converts LLM outputs into Python objects.
# Easy Validation - Uses Pydantic's built-in validation to catch incorrect or missing data.
# Seamless Integration - Works well with other LangChain components.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({'place':'sri lankan'})

print(final_result)

# Rule of thumb:

# If your LLM supports structured outputs → use with_structured_output(). 
# It’s cleaner, safer, and reduces parsing headaches.

# If your LLM does not support structured outputs → use PydanticOutputParser.