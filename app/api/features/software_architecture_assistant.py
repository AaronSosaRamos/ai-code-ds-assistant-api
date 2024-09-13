from langgraph.graph import StateGraph
from app.api.features.schemas.software_architecture_assistant_schemas import GraphState
from app.api.features.util.software_architecture_assistant_functions import (
    evaluate_architecture_quality,
    generate_architecture_description,
    suggest_architecture_improvements, 
    validate_architecture
)
from langgraph.graph import END

workflow = StateGraph(GraphState)

workflow.add_node("generate_architecture_description", generate_architecture_description)
workflow.add_node("validate_architecture", validate_architecture)
workflow.add_node("suggest_architecture_improvements", suggest_architecture_improvements)
workflow.add_node("evaluate_architecture_quality", evaluate_architecture_quality)

workflow.set_entry_point("generate_architecture_description")

workflow.add_edge('generate_architecture_description', "validate_architecture")
workflow.add_edge('validate_architecture', "suggest_architecture_improvements")
workflow.add_edge('suggest_architecture_improvements', "evaluate_architecture_quality")
workflow.add_edge('evaluate_architecture_quality', END)

def compile_workflow():
    architecture_assistant = workflow.compile()
    return architecture_assistant