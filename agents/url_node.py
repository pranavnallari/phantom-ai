# agents/url_node.py

from models import State
from langchain_ollama import ChatOllama

def node_url_scan(llm: ChatOllama) -> State:
    def node(state: State):
        return url_scan(state, llm)
    return node


def url_scan(state: State, llm: ChatOllama) -> State:
    """
    Perform a URL scan on the target URL.
    
    Args:
        state (State): The current state of the application.
        llm (ChatOllama): The language model instance for processing.
    
    Returns:
        State: Updated state after performing the URL scan.
    """
    print("Performing URL scan...")
    return state