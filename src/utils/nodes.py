from dotenv import load_dotenv
from .states import GenerateAnalystsState
from .models import llm
from .objects import Analyst ,Perspectives
from .prompts import analyst_instructions
from langchain.messages import SystemMessage, HumanMessage
from langgraph.types import interrupt
load_dotenv()

# Creating our node

def create_analysts(state:GenerateAnalystsState):
    """Create Analysts"""
    topic = state["topic"]
    max_analysts= state["max_analysts"]
    human_analyst_feedback = state.get("human_analyst_feedback","") # Just if in case human feedback is empty

    # Enforce structured output 
    structured_llm=llm.with_structured_output(Perspectives)


    # System_Message
    system_message = analyst_instructions.format(topic=topic,
                                                 human_analyst_feedback=human_analyst_feedback,
                                                 max_analysts=max_analysts)
    

    # Generate Analyst
    analysts = structured_llm.invoke([SystemMessage(content=system_message)] + [HumanMessage(content="Please Generate the set of analyst ")])

    return {"analysts": analysts.analysts}

# Human feedback -> interrupt 
def human_feedback(state:GenerateAnalystsState):
    """This is where the human gives feedback about the analysts given."""

    feedback =interrupt({
        "question": "Are these analysts okay for you?",
        "analysts": [
            # There can be possibility that the user is satisified with number of analysts already made. or with its domain -> []
            analyst.model_dump() if hasattr(analyst,"model_dump") 
            else analyst 
            for analyst in state.get("analysts",[])    
        ],
        "instructions": "Return feedback to regenerate analysts "
        "or return empty/perfect/okay/continue to approve and continue the graph"
    })

    if feedback is None:
        return {"human_analyst_feedback":None}
    if isinstance(feedback,str):
        feedback=feedback.strip()
        if feedback == "":
            return {"human_analyst_feedback":None}
        
        if feedback.lower() in {"perfect","okay","yes","ok","continue"}:
            return {"human_analyst_feedback":None}
        
        return {"human_analyst_feedback":feedback}
    
    return {"human_analyst_feedback": None}

            