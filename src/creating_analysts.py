from src.utils.nodes import create_analysts
from langgraph.graph import START , END , StateGraph
from src.utils.states import GenerateAnalystsState
from dotenv import load_dotenv

load_dotenv()

#Creating graph
# GenerateAnalystsState state


# Nodes - create_analysr


# Edges - simple 


# Graph together

builder = StateGraph(GenerateAnalystsState)

builder.add_node(create_analysts,"create_analysts")

builder.add_edge(START,"create_analysts")
builder.add_edge("create_analysts",END)

graph = builder.compile()

