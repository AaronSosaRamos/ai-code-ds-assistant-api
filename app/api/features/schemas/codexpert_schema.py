from pydantic import BaseModel, Field
from typing import List, Optional, Dict, TypedDict

class CodeInput(BaseModel):
    code: str = Field(..., description="The code provided by the user to be analyzed and optimized")
    programming_language: str = Field(..., description="The programming language of the provided code (e.g., Python, Java, etc.)")
    is_ai_related: bool = Field(None, description="Indicates if the code is related to AI, for researching design patterns using Tavily if applicable")
    context: str = Field(None, description="Optional context or description of the problem the code is addressing")

class CodeEvaluation(BaseModel):
    works: bool = Field(..., description="Indicates if the code works as expected")
    errors: Optional[List[str]] = Field(None, description="List of errors or issues found in the code execution")

class RefactoringSuggestions(BaseModel):
    suggestions: List[str] = Field(..., description="List of specific refactoring suggestions for improving the code")
    rationale: List[str] = Field(..., description="Explanation for each refactoring suggestion")

class DesignPatternResearch(BaseModel):
    design_pattern_applicable: bool = Field(..., description="Indicates if a design pattern could be applied to the code")
    pattern_name: Optional[str] = Field(None, description="Name of the design pattern that can be applied, if applicable")
    resources_found: Optional[Dict[str, str]] = Field(None, description="Links or references to external resources if research was done using Tavily")

class QualityAttributesApplication(BaseModel):
    attributes_applied: List[str] = Field(..., description="List of software quality attributes applied (e.g., SOLID principles, DRY, etc.)")
    improvements_achieved: List[str] = Field(..., description="Explanation of how each quality attribute improved the code")

class CodeOutput(BaseModel):
    optimized_code: str = Field(..., description="The optimized version of the provided code after processing")

class GraphState(TypedDict):
    code: str
    programming_language: str
    is_ai_related: bool
    context: str

    code_evaluation: CodeEvaluation

    refactoring_suggestions: RefactoringSuggestions

    design_pattern_research: DesignPatternResearch

    quality_attributes_application: QualityAttributesApplication

    optimized_code: CodeOutput