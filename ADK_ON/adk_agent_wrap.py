# adk_agent_wrap.py

from typing import Any
from graph import build_graph

graph = build_graph()

def run_my_langgraph_agent(input_data: str) -> dict[str, Any]:
    """
    Call the LangGraph agent and return structured output.
    Args:
        input_data: The task or query the graph expects.
    """
    result = graph.invoke({"input": input_data})
    return {"status": "success", "result": result}

