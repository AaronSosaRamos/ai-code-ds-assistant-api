from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import (
       AIMessage,
       HumanMessage,
       SystemMessage
  )
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from app.api.features.schemas.codexpert_schema import CodeEvaluation, CodeOutput, DesignPatternResearch, QualityAttributesApplication, RefactoringSuggestions
from app.api.logger import setup_logger

logger = setup_logger(__name__)
load_dotenv(find_dotenv())

chat_openai_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

def code_evaluation(state):
    json_parser = JsonOutputParser(pydantic_object=CodeEvaluation)

    messages = [
        SystemMessage(content=f"You are an expert in analyzing {state['programming_language']} code."),
        HumanMessage(content=f"""
        Analyze the following {state['programming_language']} code for syntax errors and logical issues:

        {state['code']}

        Context: {state.get('context', 'No additional context provided.')}

        Step-by-step reasoning:
        1. Check for syntax errors.
        2. Identify any logical issues.
        3. Determine if the code works correctly.

        The code is AI-related: {'Yes' if state['is_ai_related'] else 'No'}

        Provide a brief evaluation, listing errors, if any, and confirming if the code works as expected.

        Ensure your response follows the format and requirements specified in {json_parser.get_format_instructions()}.
        """)
    ]

    result = chat_openai_llm.invoke(messages)

    parsed_result = json_parser.parse(result.content)

    logger.info(f"Code Evaluation: {parsed_result}")

    return {
        "code_evaluation": parsed_result
    }

def generate_refactoring_suggestions(state):
    json_parser = JsonOutputParser(pydantic_object=RefactoringSuggestions)

    evaluation_summary = f"The code works correctly: {state['code_evaluation']['works']}."
    if state['code_evaluation']["errors"]:
        evaluation_summary += f" However, the following errors were identified: {', '.join(state['code_evaluation']['errors'])}."
    else:
        evaluation_summary += " No errors were found."

    messages = [
        SystemMessage(content=f"You are an expert in refactoring {state['programming_language']} code."),
        HumanMessage(content=f"""
        Given the following {state['programming_language']} code:

        {state['code']}

        Context: {state.get('context', 'No additional context provided.')}

        Code Evaluation Results: {evaluation_summary}

        Step-by-step reasoning:
        1. Identify areas for improvement in the code, considering the evaluation results.
        2. Suggest appropriate refactoring techniques.
        3. Provide a list of actionable refactoring suggestions.

        Ensure your response follows the format and requirements specified in {json_parser.get_format_instructions()}.
        """)
    ]

    result = chat_openai_llm.invoke(messages)

    parsed_result = json_parser.parse(result.content)

    logger.info(f"Refactoring Suggestions: {parsed_result}")

    return {
        "refactoring_suggestions": parsed_result,
    }

def research_design_pattern(state):
    search = TavilySearchResults(max_results=2)
    tools = [search]
    agent_executor = create_react_agent(chat_openai_llm, tools)

    json_parser = JsonOutputParser(pydantic_object=DesignPatternResearch)

    refactoring_summary = f"The following refactoring suggestions were provided: {', '.join(state['refactoring_suggestions']['suggestions'])}."

    ai_related_message = f"""
    Assess whether the following code is related to AI:

    {state['code']}

    Refactoring Suggestions: {refactoring_summary}

    Is it related to AI? {'Yes' if state['is_ai_related'] else 'No'}

    If it is about AI, use Tavily to research relevant design patterns that could support this code.
    Provide detailed information about applicable design patterns.

    If not, you must not use Tavily and just analyse the code directly for suggesting design patterns in base of what you know.

    Ensure your response follows the format and requirements specified in {json_parser.get_format_instructions()}.
    """

    messages = [
        SystemMessage(content=f"You are an expert in software design patterns, refactoring, and AI-related code."),
        HumanMessage(content=ai_related_message)
    ]

    result = agent_executor.invoke({'messages': messages})

    logger.info(result)

    parsed_result = json_parser.parse(result["messages"][-1].content)

    logger.info(f"Design Pattern Research: {parsed_result}")

    return {
        "design_pattern_research": parsed_result
    }

def apply_quality_attributes(state):
    json_parser = JsonOutputParser(pydantic_object=QualityAttributesApplication)

    if state['design_pattern_research']['design_pattern_applicable']:
        design_pattern_summary = f"A design pattern '{state['design_pattern_research']['pattern_name']}' has been suggested for this code based on AI-related research."
    else:
        design_pattern_summary = "No design pattern was applied or needed."

    refactoring_summary = f"The following refactoring suggestions were applied: {', '.join(state['refactoring_suggestions']['suggestions'])}."

    messages = [
        SystemMessage(content=f"You are an expert in software engineering and code quality improvement for {state['programming_language']} code."),
        HumanMessage(content=f"""
        Based on the following {state['programming_language']} code and its context:

        {state['code']}

        Refactoring Summary: {refactoring_summary}

        Design Pattern Research: {design_pattern_summary}

        Step-by-step reasoning:
        1. Identify which software quality attributes (e.g., SOLID principles, DRY, KISS) can be applied to improve the code.
        2. Explain how each quality attribute improves the code, with specific focus on maintainability, readability, performance, or other key aspects.
        3. Provide a clear explanation for how these quality attributes interact with the refactoring and any design patterns applied.

        Ensure your response follows the format and requirements specified in {json_parser.get_format_instructions()}.
        """)
    ]

    result = chat_openai_llm.invoke(messages)

    parsed_result = json_parser.parse(result.content)

    logger.info(f"Quality Attributes Applied: {parsed_result}")

    return {
        "quality_attributes_application": parsed_result
    }

def generate_optimized_code(state):
    json_parser = JsonOutputParser(pydantic_object=CodeOutput)

    refactoring_summary = f"The following refactoring suggestions were applied: {', '.join(state['refactoring_suggestions']['suggestions'])}."

    if state['design_pattern_research']['design_pattern_applicable']:
        design_pattern_summary = f"A design pattern '{state['design_pattern_research']['pattern_name']}' was suggested and applied to enhance the structure of the code."
    else:
        design_pattern_summary = "No design pattern was applied or needed."

    quality_attributes_summary = f"Quality attributes such as {', '.join(state['quality_attributes_application']['attributes_applied'])} were applied to further improve the code."

    messages = [
        SystemMessage(content=f"You are an expert in code optimization for {state['programming_language']} code."),
        HumanMessage(content=f"""
        Based on the previous analysis, refactoring, and design improvements, please generate an optimized version of the following {state['programming_language']} code:

        {state['code']}

        Refactoring Summary: {refactoring_summary}

        Design Pattern Research: {design_pattern_summary}

        Quality Attributes: {quality_attributes_summary}

        Return the final optimized version of the code, taking into account all previous suggestions and improvements.

        Ensure your response follows the format and requirements specified in {json_parser.get_format_instructions()}.
        """)
    ]

    result = chat_openai_llm.invoke(messages)

    parsed_result = json_parser.parse(result.content)

    logger.info(f"Optimized Code: {parsed_result}")

    return {
        "optimized_code": parsed_result
    }