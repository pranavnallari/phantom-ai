# models/schema.py

from typing import Annotated, TypedDict, Literal, Optional


class State(TypedDict):
    run_id: Annotated[str, "Unique identifier for the run"]
    raw_input: Annotated[str, "Raw input from the user"]
    target_type: Annotated[Optional[Literal["ip", "domain", "url"]], "Type of the target to extract"]
    orig_target_value: Annotated[Optional[str], "Original target value extracted from the input"]
    target_value: Annotated[Optional[str], "Extracted target value"]
    tasks: Annotated[Optional[list], "List of tasks to perform"]
    tool_outputs: Annotated[Optional[dict[str, str]], "Outputs from tools used in the tasks"]
    report: Annotated[Optional[str], "Generated report based on the tasks performed"]
    has_error: Annotated[bool, "Indicates if there was an error"]
    error_message: Annotated[Optional[str], "Error message if any"]