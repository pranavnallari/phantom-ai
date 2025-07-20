# agents/url_node.py

from models import State
from langchain_ollama import ChatOllama
from .map import task_tool_map
from tools import get_docker_client
from urllib.parse import urlparse


def node_url_scan(llm: ChatOllama) -> State:
    def node(state: State):
        return url_scan(state, llm)
    return node

def url_scan(state: State, llm: ChatOllama) -> State:
    """
    Perform a URL scan on the target URL.
    """
    print("Performing URL scan...")
    if state["has_error"] or state["target_type"] != "url":
        return state

    client = get_docker_client()
    target = state["target_value"]

    # Run URL-specific tasks
    tasks = state["tasks"] or ["web_tech", "dir_enum", "vuln_scan", "dns_lookup", "whois", "port_scan"]

    for task in tasks:
        if task in ["web_tech", "dir_enum", "vuln_scan"]:
            try:
                result = task_tool_map[task](target, client)
                state["tool_outputs"][task] = result
            except Exception as e:
                state["tool_outputs"][task] = f"{task} failed: {str(e)}"

    # Decompose into domain for next pass
    if any(task in tasks for task in ["dns_lookup", "whois", "port_scan"]):
        parsed = urlparse(target)
        domain = parsed.hostname
        if domain:
            state["target_type"] = "domain"
            state["target_value"] = domain
        else:
            state["has_error"] = True
            state["error_message"] = f"Failed to extract domain from URL: {target}"

    return state
