# agents/ip_node.py

from models import State
from langchain_ollama import ChatOllama
from .map import task_tool_map
from tools import get_docker_client

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
    
    if state["has_error"] or state["target_type"] != "ip":
        return state

    if not state["tasks"] or "port_scan" in state["tasks"]:
        client = get_docker_client()
        output = task_tool_map["port_scan"](state["target_value"], client)
        state["tool_outputs"]["port_scan"] = output

    
    return state