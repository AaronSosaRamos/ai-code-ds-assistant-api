from langgraph.graph import StateGraph
from app.api.features.schemas.codexpert_schema import GraphState
from langgraph.graph import END

from app.api.features.util.codexpert_functions import (
    code_evaluation,
    generate_refactoring_suggestions,
    research_design_pattern,
    apply_quality_attributes,
    generate_optimized_code
)

workflow = StateGraph(GraphState)

workflow.add_node("code_evaluation_node", code_evaluation)
workflow.add_node("generate_refactoring_suggestions", generate_refactoring_suggestions)
workflow.add_node("research_design_pattern", research_design_pattern)
workflow.add_node("apply_quality_attributes", apply_quality_attributes)
workflow.add_node("generate_optimized_code", generate_optimized_code)

workflow.set_entry_point("code_evaluation_node")

workflow.add_edge('code_evaluation_node', "generate_refactoring_suggestions")
workflow.add_edge('generate_refactoring_suggestions', "research_design_pattern")
workflow.add_edge('research_design_pattern', "apply_quality_attributes")
workflow.add_edge('apply_quality_attributes', "generate_optimized_code")

workflow.add_edge('generate_optimized_code', END)

def compile_workflow():
    codexpert = workflow.compile()
    return codexpert