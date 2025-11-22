from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY
from typing import List


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0.1,
    max_tokens=1000,
    max_retries=3
)

itinerary_prompt = ChatPromptTemplate([
    ("system","You are a helpful travel assistant. Create a day trip itinary for {city} based on users interest : {interests}. Provide a brief, bullet itineary"),
    ("human","Create a itineary for my day trip")
])

def generate_itineary(city:str, interests:List[str]) -> str:
    response = llm.invoke(
        itinerary_prompt.format_messages(city=city, interests=', '.join(interests))
    )
    return response.content