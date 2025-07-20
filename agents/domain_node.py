# agents/domain_node.py

from models import State
from langchain_ollama import ChatOllama
from tools import get_docker_client
import socket
from .map import task_tool_map
def node_domain_scan(llm : ChatOllama) -> State:
    def node(state : State):
        return domain_scan(state, llm)
    return node


def domain_scan(state: State, llm: ChatOllama) -> State:
    if state["has_error"] or state["target_type"] != "domain":
        return state

    print("Performing domain scan...")
    client = get_docker_client()
    target = state["target_value"]

    tasks = ["whois", "dns_lookup", "port_scan"]

    for task in tasks:
        if task in ["whois", "dns_lookup"]:
            try:
                result = task_tool_map[task](target, client)
                state["tool_outputs"][task] = result
            except Exception as e:
                state["tool_outputs"][task] = f"{task} failed: {str(e)}"
    print(f"Domain scan completed for {target}")
    if "port_scan" in tasks:
        try:
            extracted_ip = socket.gethostbyname(target)
            state["target_type"] = "ip"
            state["target_value"] = extracted_ip
        except socket.gaierror as e:
            state["has_error"] = True
            state["error_message"] = f"Failed to resolve IP for domain '{target}': {str(e)}"

    return state

