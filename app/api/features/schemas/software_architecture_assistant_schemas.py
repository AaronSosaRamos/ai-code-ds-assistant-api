from pydantic import BaseModel, Field
from typing import List, Optional
from typing import Dict

class SoftwareArchitectureAssistantArgs(BaseModel):
    img_url: str
    requirements: str
    lang: str

class Component(BaseModel):
    name: str = Field(..., description="The name of the component, such as 'API Gateway' or 'Database'.")
    description: Optional[str] = Field(None, description="A brief description of the component's purpose.")
    dependencies: List[str] = Field([], description="List of other components that this component depends on.")
    type_component: str = Field(..., description="The type of component, e.g., 'Service', 'Database', 'Event', etc.")
    exposed_endpoints: Optional[List[str]] = Field(None, description="A list of endpoints exposed by this component, if applicable.")
    input_data: Optional[List[str]] = Field(None, description="Data consumed by this component.")
    output_data: Optional[List[str]] = Field(None, description="Data produced by this component.")

class ArchitectureSchema(BaseModel):
    architecture_name: str = Field(..., description="The name of the architecture, such as 'Microservices', '3-Tier', 'Event-Driven' and so forth.")
    layers: List[str] = Field(..., description="The different layers in the architecture, e.g., 'Presentation', 'Business Logic', 'Data'.")
    components: List[Component] = Field(..., description="The components that make up the architecture.")
    external_services: Optional[List[str]] = Field(None, description="List of external services or third-party APIs integrated with the system.")
    events: Optional[List[str]] = Field(None, description="A list of events that trigger actions in the system, if applicable.")
    data_flow_description: Optional[str] = Field(None, description="A description of how data flows through the architecture.")

class Requirement(BaseModel):
    name: str = Field(..., description="The name of the requirement.")
    description: Optional[str] = Field(None, description="A brief description of the requirement.")
    must_have_layers: List[str] = Field(..., description="A list of layers that the architecture must include.")
    must_have_components: List[str] = Field(..., description="A list of specific components the architecture must have.")
    must_have_services: Optional[List[str]] = Field(None, description="List of external services the architecture must integrate.")
    must_handle_events: Optional[List[str]] = Field(None, description="List of events that the architecture must handle.")

class ArchitectureValidationSchema(BaseModel):
    architecture: ArchitectureSchema = Field(..., description="The architecture being validated.")
    requirements: List[Requirement] = Field(..., description="The list of requirements that the architecture must meet.")

class ImprovementSuggestion(BaseModel):
    suggestion: str = Field(..., description="The suggested improvement for the architecture.")
    details: Optional[str] = Field(None, description="Additional details about how to implement the suggestion.")

class ArchitectureImprovementSchema(BaseModel):
    architecture: ArchitectureSchema = Field(..., description="The architecture being evaluated.")
    requirements: List[Requirement] = Field(..., description="The list of requirements for the architecture.")
    suggestions: Optional[List[ImprovementSuggestion]] = Field([], description="A list of improvement suggestions based on unmet requirements.")

class QualityAttribute(BaseModel):
    attribute_name: str = Field(..., description="The name of the quality attribute, such as 'Scalability', 'Security', or 'Performance'.")
    description: Optional[str] = Field(None, description="A brief description of the quality attribute.")
    current_status: str = Field(..., description="The current implementation status of this quality attribute in the architecture, e.g., 'Implemented', 'Partially Implemented', 'Not Implemented'.")
    implementation_details: Optional[str] = Field(None, description="Details on how this attribute is implemented or how it can be improved.")
    priority: int = Field(..., ge=1, le=5, description="Priority of this attribute from 1 (low) to 5 (high).")

class QualityAttributesSchema(BaseModel):
    architecture: ArchitectureSchema = Field(..., description="The architecture to which quality attributes are being added.")
    quality_attributes: List[QualityAttribute] = Field(..., description="A list of quality attributes applied to the architecture.")
    quality_evaluation: Dict[str, int] = Field(None, description="Evaluation of the quality attributes' implementation status.")

from typing import Dict, TypedDict, Optional

class GraphState(TypedDict):
    img_url: str
    requirements: str
    lang: str

    detected_architecture: ArchitectureSchema

    architecture_with_requirements: ArchitectureValidationSchema

    improved_architecture: ArchitectureImprovementSchema

    architecture_with_quality_attributes: QualityAttributesSchema