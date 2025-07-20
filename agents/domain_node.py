# agents/domain_node.py

from models import State
from langchain_ollama import ChatOllama


def node_domain_scan(llm : ChatOllama) -> State:
    def node(state : State):
        return domain_scan(state, llm)
    return node


def domain_scan(state: State, llm: ChatOllama) -> State:    
    """
    Perform a domain scan on the target domain.
    
    Args:
        state (State): The current state of the application.
        llm (ChatOllama): The language model instance for processing.
    
    Returns:
        State: Updated state after performing the domain scan.
    """
    print("Performing domain scan...")
    return state