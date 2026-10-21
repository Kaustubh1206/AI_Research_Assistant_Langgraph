from typing import NotRequired, Optional, List
from typing_extensions import TypedDict
from .objects import Analyst


# State
class GenerateAnalystsState(TypedDict):
    """"""
    topic: str # Research topic 
    max_analysts: int # Number of analysts
    human_analyst_feedback: NotRequired[Optional[str]] # human feedback for what is generated
    analysts: NotRequired[List[Analyst]] # List of all our Analysts