# agent.py

import os
from langchain.chat_models import ChatOpenAI
from google.adk.agents import Agent
from typing import Any
from google.adk.agents import Agent
from graph import build_graph
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from tools import load_tools
from google.adk.tools import FunctionTool


load_dotenv()
graph = build_graph()


# def run_my_langgraph_agent(input_data: str) -> dict[str, Any]:
#     """Invoke the LangGraph pipeline and return structured output."""
#     result = graph.invoke({"input": input_data})  # adapt schema if needed
#     return {"status": "success", "result": result}


def run_my_langgraph_agent(input_data: str) -> dict[str, Any]:
    """
    Invoke the LangGraph pipeline and return a plain text answer.
    Always return JSON-serializable data so ADK can emit tool messages.
    """
    try:
        out = graph.invoke({"messages": [("user", input_data)]})
        # Extract a safe, serializable answer
        answer = None
        if isinstance(out, dict) and "messages" in out and out["messages"]:
            last = out["messages"][-1]
            answer = getattr(last, "content", str(last))
        else:
            answer = str(out)
        return {"status": "success", "answer": answer}
    except Exception as e:
        # Return an error payload instead of raising to keep the tool pipeline intact
        return {"status": "error", "error": str(e)}

root_agent = Agent(
  model=LiteLlm(model="openai/gpt-4o"),
  name="my_integrated_agent",
  description="Delegates tasks to a LangGraph Runnable through a function tool.",
  instruction="Use run_my_langgraph_agent when the graph is better suited.",
  tools=[run_my_langgraph_agent],
    )

