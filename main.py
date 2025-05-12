# Import the AgentRearrange class for coordinating multiple agents
from swarms import AgentRearrange

# Import specialized medical agents for different aspects of patient care
from multi_agent_rag.agents import (
    education_security_advisor,  # Agent for educational security
    financial_security_specialist,  # Agent for financial security
    healthcare_security_analyst,  # Agent for healthcare security
    manufacturing_security_expert,  # Agent for manufacturing security
    energy_grid_security_analyst, 
    government_security_specialist,
    incident_response_coordinator,
    retail_security_advisor,
    telecommunications_security_expert,
    transportation_security_expert


)

# Import database class for storing and retrieving medical documents
from multi_agent_rag.memory import LlamaIndexDB

# Initialize the SwarmRouter to coordinate the medical agents
router = AgentRearrange(
    name="cybersecurity-expert-swarm",
    description="Collaborative cybersecurity team for comprehensive threat analysis and response planning",
    max_loops=1,  # Limit to one iteration through the agent flow
    agents=[
    education_security_advisor,  # Agent for educational security
    financial_security_specialist,  # Agent for financial security
    healthcare_security_analyst,  # Agent for healthcare security
    manufacturing_security_expert,  # Agent for manufacturing security
    energy_grid_security_analyst, 
    government_security_specialist,
    incident_response_coordinator,
    retail_security_advisor,
    telecommunications_security_expert,
    transportation_security_expert
    ],
    # Configure the document storage and retrieval system
    memory_system=LlamaIndexDB(
        data_dir="docs",  # Directory containing medical documents
        filename_as_id=True,  # Use filenames as document identifiers
        recursive=True,  # Search subdirectories
        # required_exts=[".txt", ".pdf", ".docx"],  # Supported file types
        similarity_top_k=10,  # Return top 10 most relevant documents
    ),
    # Define the sequential flow of information between agents
    flow=
    flow=f"{medical_data_extractor.agent_name} -> {diagnostic_specialist.agent_name} -> {treatment_planner.agent_name} -> {specialist_consultant.agent_name} -> {patient_care_coordinator.agent_name}",
)

# Example usage
if __name__ == "__main__":
    # Run a comprehensive medical analysis task for patient Lucas Brown
    router.run(
        "Analyze this Lucas Brown's medical data to provide a diagnosis and treatment plan"
    )
