from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os
from app.api.features.schemas.schemas import ChatMessage, Message

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def read_text_file(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    absolute_file_path = os.path.join(script_dir, file_path)
    
    with open(absolute_file_path, 'r') as file:
        return file.read()

def build_prompt():
    """
    Build the prompt for the model.
    """
    
    template = read_text_file("prompt/chatbot-prompt.txt")
    prompt = PromptTemplate(
        template=template,
        input_variables=["text"],
    )
    
    return prompt


def chatbot_executor(user_name: str, user_query: str, messages: list[Message], k=10):
    
    # create a memory list of last k = 3 messages
    chat_context = [
        ChatMessage(
            role=message.role, 
            type=message.type, 
            text=message.payload.text
        ) for message in messages[-k:]
    ]

    prompt = build_prompt()
    
    llm = GoogleGenerativeAI(model="gemini-1.5-flash") 
    
    chain =  prompt | llm
    
    response = chain.invoke({"chat_history": chat_context, "user_name": user_name, "user_query": user_query})
    
    return response
