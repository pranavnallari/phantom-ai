#tools/init.py

import uuid
from models import State

def create_initial_state(input_text: str) -> State:
    """
    Creates the initial state for the input parsing process.
    Args:
        input_text (str): The input text to be processed.
    Returns:
        State: The initial state containing the run ID and raw input.
    """
    return State({
        "run_id": str(uuid.uuid4()),
        "raw_input": input_text,
        "has_error": False,
    })