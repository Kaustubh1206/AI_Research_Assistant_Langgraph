from typing import Literal
from dotenv import load_dotenv
from .states import GenerateAnalystsState
from langgraph.graph import END
load_dotenv()

# Conditional Edges
def should_continue(state:GenerateAnalystsState)-> Literal["create_analysts",END]:
    """Return the next node to execute"""
    human_analyst_feedback = state.get("human_analyst_feedback", None)

    if human_analyst_feedback:
        return "create_analysts"
    return END