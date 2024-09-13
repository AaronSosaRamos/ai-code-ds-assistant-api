
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import (
       AIMessage,
       HumanMessage,
       SystemMessage
  )
from langchain_google_genai import ChatGoogleGenerativeAI
from app.api.features.schemas.software_architecture_assistant_schemas import (
    ArchitectureImprovementSchema,
    ArchitectureValidationSchema,
    ArchitectureSchema,
    QualityAttributesSchema, 

)
from langchain_core.output_parsers import JsonOutputParser

load_dotenv(find_dotenv())

chat_openai_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
google_chat_genai_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def generate_architecture_description(state):
    parser = JsonOutputParser(pydantic_object=ArchitectureSchema)

    lang_message = {
        "en": "Analyze the image and give me the architecture description with the following details: architecture name, layers, components, external services, events, and data flow description.",
        "es": "Analiza la imagen y dame la descripción de la arquitectura con los siguientes detalles: nombre de la arquitectura, capas, componentes, servicios externos, eventos y descripción del flujo de datos.",
        "fr": "Analyse l'image et donne-moi la description de l'architecture avec les détails suivants : nom de l'architecture, couches, composants, services externes, événements et description du flux de données.",
        "de": "Analysiere das Bild und gib mir die Architektur-Beschreibung mit folgenden Details: Architekturname, Schichten, Komponenten, externe Dienste, Ereignisse und Beschreibung des Datenflusses.",
        "pt": "Analise a imagem e me dê a descrição da arquitetura com os seguintes detalhes: nome da arquitetura, camadas, componentes, serviços externos, eventos e descrição do fluxo de dados."
    }

    message_content = [
        {
            "type": "text",
            "text": lang_message.get(state["lang"], lang_message["en"])
        },
        {"type": "image_url", "image_url": state["img_url"]},
        {"type": "text", "text": f"Format the response in this format: {parser.get_format_instructions()}"}
    ]

    message = HumanMessage(content=message_content)

    response = google_chat_genai_llm.invoke([message]).content

    detected_architecture = parser.parse(response)

    print(f"Architecture Description: {detected_architecture}")

    return {
        "detected_architecture": detected_architecture
    }

def validate_architecture(state):
    json_parser = JsonOutputParser(pydantic_object=ArchitectureValidationSchema)

    lang = state['lang']
    detected_architecture = state['detected_architecture']
    requirements = state['requirements']

    messages = [
        SystemMessage(content=f"You are an expert in software architecture validation for {lang} systems."),
        HumanMessage(content=f"""Please validate the detected architecture against the following requirements.
        Make sure to identify any missing layers, components, services, or events.

        Detected Architecture:
        {detected_architecture}

        Requirements:
        {requirements}

        Respond with suggestions for improvement or state if the architecture fully meets the requirements. Ensure your response follows the format specified in {json_parser.get_format_instructions()}.
        """)
    ]

    result = chat_openai_llm.invoke(messages)

    parsed_result = json_parser.parse(result.content)

    print(f"Architecture Validation Result: {parsed_result}")

    return {
        "architecture_with_requirements": parsed_result
    }

def suggest_architecture_improvements(state):
    json_parser = JsonOutputParser(pydantic_object=ArchitectureImprovementSchema)

    architecture_with_requirements = state['architecture_with_requirements']
    requirements = state['requirements']
    lang = state["lang"]

    messages = [
        SystemMessage(content=f"You are an expert in software architecture improvement for {lang} systems."),
        HumanMessage(content=f"""Please analyze the provided architecture and offer improvement suggestions based on the following requirements.
        Focus on missing or suboptimal layers, components, services, or event handling, and provide specific recommendations.

        Architecture:
        {architecture_with_requirements}

        Requirements:
        {requirements}

        Respond with suggestions for improvement. Ensure your response follows the format specified in {json_parser.get_format_instructions()}.
        """)
    ]

    result = chat_openai_llm.invoke(messages)

    parsed_result = json_parser.parse(result.content)

    print(f"Architecture Improvement Suggestions: {parsed_result}")

    return {
        "improved_architecture": parsed_result
    }

def evaluate_architecture_quality(state):
    json_parser = JsonOutputParser(pydantic_object=QualityAttributesSchema)

    improved_architecture = state['improved_architecture']
    lang = state['lang']

    messages = [
        SystemMessage(content=f"You are an expert in software architecture quality assessment for {lang} systems."),
        HumanMessage(content=f"""Please analyze the provided architecture and evaluate its quality attributes.
        Focus on scalability, security, performance, and maintainability, and indicate whether these attributes are implemented, partially implemented, or not implemented.

        Architecture:
        {improved_architecture}

        Respond with a detailed evaluation of the quality attributes and ensure your response follows the format specified in {json_parser.get_format_instructions()}.
        """)
    ]

    result = chat_openai_llm.invoke(messages)

    parsed_result = json_parser.parse(result.content)

    print(f"Architecture Quality Evaluation: {parsed_result}")

    return {
        "architecture_with_quality_attributes": parsed_result
    }

