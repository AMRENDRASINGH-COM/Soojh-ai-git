# graph.py

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from node import chatbot, tools, State

def build_graph():
    graph_builder = StateGraph(State)

    # Add chatbot and tool nodes
    graph_builder.add_node("chatbot", chatbot)
    tool_node = ToolNode(tools=tools)
    graph_builder.add_node("tools", tool_node)

    # Define graph flow
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_conditional_edges("chatbot", tools_condition)
    graph_builder.add_edge("tools", "chatbot")
    graph_builder.add_edge("chatbot", END)

    return graph_builder.compile()
    
# graph = build_graph()

# def run_my_langgraph_agent(input_data: str) -> str:
#     events = graph.stream({"messages": [("user", input_data)]}, stream_mode="values")
#     response = ""
#     for event in events:
#         response = event["messages"][-1].content
#     return response
