from models import State

def route_request(state: State) -> str:
    """
    Route the request based on the target type.
    """
    if state["has_error"]:
        print(f"Error occurred {state['error_message']}")
        return "error"
    print(f"Routing request for target type: {state['target_type']}")
    print(f"Serviced identified : {state['tasks']}")
    return state["target_type"]