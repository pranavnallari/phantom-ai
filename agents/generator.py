# agents/generator.py

from models import State
from langchain_ollama import ChatOllama
from report import *
import os


def node_report_generator(llm : ChatOllama) -> State:
    """
    Generates a report for the node using the provided LLM.
    
    Args:
        llm (ChatOllama): The language model to use for generating the report.
    
    Returns:
        State: The state containing the generated report.
    """
    def node(state : State):
        return generate_report(state, llm)
    return node


def get_summary_prompt(task: str, raw_output: str) -> str:    
    """
    Generate a summary prompt for the given task and raw output.
    
    Args:
        task (str): The task for which to generate the summary.
        raw_output (str): The raw output from the task.
    Returns:
        str: The generated summary prompt.
    """
    if task == "port_scan":
        return PORT_SCAN_SUMMARY_PROMPT + raw_output
    elif task == "web_tech":
        return WEB_TECH_SUMMARY_PROMPT + raw_output
    elif task == "vuln_scan":
        return VULN_SCAN_SUMMARY_PROMPT + raw_output
    elif task == "dns_lookup":
        return DNS_LOOKUP_SUMMARY_PROMPT + raw_output
    elif task == "whois":
        return WHOIS_SUMMARY_PROMPT + raw_output
    elif task == "dir_enum":
        return DIR_ENUM_SUMMARY_PROMPT + raw_output
    return None

def generate_report(state: State, llm : ChatOllama) -> State:
    """
    Generate a report based on the current state.
    
    Args:
        state (State): The current state of the application.
        llm (ChatOllama): The language model instance for processing.

    Returns:
        State: Updated state after generating the report.
    """
    
    print("Generating report...")
    
    if state["has_error"]:
        return state

    summaries = {}
    for task, raw_output in state["tool_outputs"].items():
        prompt = get_summary_prompt(task, raw_output)
        summary = llm.invoke(prompt)
        summaries[task] = summary.content.strip()
        
    combined = "\n\n".join(summaries.values())
    
    overall_summary = llm.invoke(OVERALL_SUMMARY_PROMPT.format(tool_summaries=combined)).content.strip()
    
    report_str = REPORT_TEMPLATE.format(
        target_value=state["orig_target_value"],
        run_id=state["run_id"],
        summary=overall_summary,
        port_scan_summary=summaries.get("port_scan", "") if summaries.get("port_scan") else "",
        port_scan_raw=state["tool_outputs"].get("port_scan", "") if state["tool_outputs"].get("port_scan") else "",
        web_tech_summary=summaries.get("web_tech", "") if summaries.get("web_tech") else "",
        web_tech_raw=state["tool_outputs"].get("web_tech", "") if state["tool_outputs"].get("web_tech") else "",
        dns_lookup_summary=summaries.get("dns_lookup", "") if summaries.get("dns_lookup") else "",
        dns_lookup_raw=state["tool_outputs"].get("dns_lookup", "") if state["tool_outputs"].get("dns_lookup") else "",
        vuln_scan_summary=summaries.get("vuln_scan", "") if summaries.get("vuln_scan") else "",
        vuln_scan_raw=state["tool_outputs"].get("vuln_scan", "") if state["tool_outputs"].get("vuln_scan") else "",
        whois_summary=summaries.get("whois", "") if summaries.get("whois") else "",
        whois_raw=state["tool_outputs"].get("whois", "") if state["tool_outputs"].get("whois") else "",
        dir_enum_summary=summaries.get("dir_enum", "") if summaries.get("dir_enum") else "",
        dir_enum_raw=state["tool_outputs"].get("dir_enum", "") if state["tool_outputs"].get("dir_enum") else ""
    )
            
    state["report"] = report_str
    
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    filename = f"{state['target_value'].replace(':', '_').replace('/', '_')}_{state['run_id']}.md"
    filepath = os.path.join(report_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_str)
    return state