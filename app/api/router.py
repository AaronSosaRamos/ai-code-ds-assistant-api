from fastapi import APIRouter, Depends
from app.api.features.chatbot import chatbot_executor
from app.api.features.schemas.schemas import ChatRequest, ChatResponse, Message
from app.api.features.schemas.software_architecture_assistant_schemas import SoftwareArchitectureAssistantArgs
from app.api.features.software_architecture_assistant import compile_workflow
from app.api.logger import setup_logger
from app.api.auth.auth import key_check


from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

logger = setup_logger(__name__)
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/chat", response_model=ChatResponse)
async def chat( request: ChatRequest, _ = Depends(key_check) ):
    user_name = request.user.fullName
    chat_messages = request.messages
    user_query = chat_messages[-1].payload.text
    
    response = chatbot_executor(user_name=user_name, user_query=user_query, messages=chat_messages)
    
    formatted_response = Message(
        role="ai",
        type="text",
        payload={"text": response}
    )
    
    return ChatResponse(data=[formatted_response])

@router.post("/software-architecture-assistant")
async def software_architecture_assistant( request: SoftwareArchitectureAssistantArgs, _ = Depends(key_check) ):
    
    try:
        logger.info(f"Image URL loaded: {request.img_url}")

        architecture_assistant = compile_workflow()
        result = architecture_assistant.invoke(
            {
                "img_url": request.img_url,
                "requirements": request.requirements,
                "lang": request.lang
            }
        )
    
    except Exception as e:
        error_message = f"Error in executor: {e}"
        logger.error(error_message)
        raise ValueError(error_message)
    
    return result
    
    return 