# CHATBOT.PY

from graph import build_graph
from node import State

# Build and compile LangGraph
graph = build_graph()

def chat_with_bot(user_input: str):
    events = graph.stream({"messages": [("user", user_input)]}, stream_mode="values")
    response = ""
    for event in events:
        response = event["messages"][-1].content
    return response

if __name__ == "__main__":
    print("🤖 Welcome to My ChatBot! Type 'exit' or 'quit' to leave.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break
        response = chat_with_bot(user_input)
        print(f"Bot: {response}")
