# node.py

import os
from dotenv import load_dotenv
from typing import Annotated
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Import tools from tools.py
from tools import load_tools

tools = load_tools()

# Initialize LLM
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)

# Shared state type
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Chatbot node function
def chatbot(state: State) -> dict:
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Expose tools and State type
__all__ = ["chatbot", "tools", "State"]
