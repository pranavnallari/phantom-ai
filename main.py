# main.py

from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END


from agents import node_parse_input, node_ip_scan, node_domain_scan, node_url_scan, route_request, node_report_generator
from models import State
from tools import create_initial_state
from config import setup_logging
from dotenv import load_dotenv



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
    load_dotenv()
    
    logger = setup_logging()
    llm = ChatOllama(model="nous-hermes2")
    graph_builder = StateGraph(State)
    logger.info(f"Initial state created")
    
    input_text = valid_inputs[5]
    
    
    graph_builder.add_node("parse_input", node_parse_input(llm))
    
    graph_builder.add_node("ip_scan", node_ip_scan(llm))
    graph_builder.add_node("domain_scan", node_domain_scan(llm))
    graph_builder.add_node("url_scan", node_url_scan(llm))
    
    graph_builder.add_node("report_generator", node_report_generator(llm))
    
    graph_builder.add_edge(START, "parse_input")
    graph_builder.add_conditional_edges("parse_input",
                                        route_request,
                                        {
                                            "ip": "ip_scan",
                                            "domain": "domain_scan",
                                            "url": "url_scan",
                                            "error": END
                                        })
    graph_builder.add_edge("ip_scan", "report_generator")
    graph_builder.add_edge("url_scan", "domain_scan")
    graph_builder.add_edge("domain_scan", "ip_scan")
    graph_builder.add_edge("report_generator", END)
    
    state = create_initial_state(input_text)
    logger.info(f"Initial state created")    
        
    graph = graph_builder.compile()
    logger.info("Graph compiled successfully")
        
        
        
    result = graph.invoke(state)
    print(result["tool_outputs"])

    
    
if __name__ == "__main__":
    main()
