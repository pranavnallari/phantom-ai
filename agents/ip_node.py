# agents/ip_node.py

from models import State
from langchain_ollama import ChatOllama

def node_ip_scan(llm : ChatOllama) -> State:
    def node(state : State):
        return ip_scan(state, llm)
    return node


def ip_scan(state: State, llm: ChatOllama) -> State:
    """
    Perform an IP scan on the target IP address.
    
    Args:
        state (State): The current state of the application.
        llm (ChatOllama): The language model instance for processing.
    
    Returns:
        State: Updated state after performing the IP scan.
    """
    
    print("Performing IP scan...")
    return state