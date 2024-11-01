import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_together import ChatTogether
from pydantic import BaseModel, Field, ValidationError
from typing import Optional

load_dotenv()
API_KEY: Optional[str] = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is missing. Please set it in the environment variables.")

class Classification(BaseModel):
    """Data model for text classification."""
    topic: str = Field(
        description="The topic of the text",
        enum=["sports", "politics", "entertainment", "technology"]
    )

def initialize_llm(api_key: str) -> ChatTogether:
    """Initializes and returns the LLM model with the given API key."""
    return ChatTogether(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0,
        api_key=api_key
    )

def create_prompt_template() -> ChatPromptTemplate:
    """Creates and returns a prompt template for classification."""
    return ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert in classifying text based on the topic. \
             Please classify the following text."),
            ("human", "{input}"),
        ]
    )

def classify_text(input_text: str) -> Classification:
    """Classifies text based on topic."""
    llm = initialize_llm(API_KEY)
    prompt_template = create_prompt_template()
    
    structured_llm = llm.with_structured_output(Classification)
    classifier_chain = prompt_template | structured_llm
    
    try:
        response = classifier_chain.invoke({"input": input_text})
    except ValidationError as e:
        print(f"Error during classification: {e}")
        raise
    
    response = {'topic': response.topic}
    return response
