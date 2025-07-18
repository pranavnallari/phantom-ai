# agents/input_parser.py

from prompts import prompt_input_parsing
from models import State
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import json



def parse_input(input_text : str, llm : ChatOllama) -> State:
    """
    Parses the input text for the target and tasks and return the State.
    
    Args:
        input_text (str): The input text to parse.
        llm (ChatOllama): The language model to use for parsing.

    Returns:
        State : The state containing the parsed information.
    """
    
    system_message = SystemMessage(content=prompt_input_parsing)
    human_message = HumanMessage(content=input_text)
    
    messages = [system_message, human_message]
    response = llm.invoke(messages)
    
    try:
        parsed_data = json.loads(response.content)
    except json.JSONDecodeError as e:
        return State({"has_error": True,
                      "error_message": f"Failed to parse response: {str(e)}"})
    return State({
        "target_type": parsed_data.get("target_type"),
        "target_value": parsed_data.get("target_value"),
        "tasks": parsed_data.get("tasks", []),
        "tool_outputs": {},
        "has_error": parsed_data.get("has_error", False),
        "error_message": parsed_data.get("error_message", None)
    })
    
    
    
def node_parse_input(llm: ChatOllama) -> State:
    """
    Node function to parse input in the state graph.
    
    Args:
        llm : Factory function to pass down llm to lower functions.
    
    Returns:
        State: The updated state with parsed information.
    """
    def node(state: State) -> State: 
        return parse_input(state["raw_input"], llm)
    return node