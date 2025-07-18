# main.py

from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END


from agents import node_parse_input
from models import State
from tools import create_initial_state
from config import setup_logging


valid_inputs = [
    "Scan 192.168.1.1 for open ports and identify web tech if any",
    "Perform a scan on example.com",
    "Check http://testsite.org for technologies and open ports",
    "Run reconnaissance on 8.8.8.8",
    "Analyze the domain github.com",
    "Investigate https://openai.com and get DNS and WHOIS info",
    "Check technologies used by http://subdomain.example.com/path/page?query=1"
]
edge_case_inputs = [
    "Scan this: example.com, and also test 192.168.0.1",  # multiple targets
    "Check the website",                                  # vague, no target
    "Give me details about 300.300.300.300",              # invalid IP
    "Perform a scan on ftp://example.com",                # unsupported protocol
    "Find tech behind www.example without extension",     # malformed domain
    "http://",                                            # malformed URL
]

def main():
    logger = setup_logging()
    llm = ChatOllama(model="nous-hermes2")
    graph_builder = StateGraph(State)
    logger.info(f"Initial state created")
    
    input_text = valid_inputs[0]
    
    graph_builder.add_node("parse_input", node_parse_input(llm))    
    graph_builder.add_edge(START, "parse_input")
    graph_builder.add_edge("parse_input", END)
    
    
    state = create_initial_state(input_text)
    logger.info(f"Initial state created")    
        
    graph = graph_builder.compile()
    logger.info("Graph compiled successfully")
        
    result = graph.invoke(state)
    print(result)
        
if __name__ == "__main__":
    
    main()
