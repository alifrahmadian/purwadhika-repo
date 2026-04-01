from graph.workflow import ShoppingAssistantGraph
from langgraph.graph import StateGraph

def chatbot(graph: StateGraph):
    app = graph.compile()

    while True:
        user_input = input("Anda: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Terima kasih telah berkunjung! Sampai jumpa lagi!")
            break

        result = app.invoke({
            "messages": [
                {"role": "user", "content": user_input}
            ],
            "history": [],
        })

        print("Chatbot:", result["messages"][-1].content)

def chatbot_stream(graph: StateGraph):
    app = graph.compile()

    while True:
        user_input = input("Anda: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Terima kasih telah berkunjung! Sampai jumpa lagi!")
            break

        for output in app.stream({
            "messages": [
                {"role": "user", "content": user_input},
            ],
            "history": [],
        }):
            for key, value in output.items():
                if key == "filter_agent":
                    next_agent = value["messages"][0].content.strip().lower()
                    if next_agent not in ["product", "promo"]:
                        next_agent = "basic"
                    print(f"🔀 Routing ke agent {next_agent}")
                else:
                    print(f"🤖 {key}:\n{value['messages'][0].content}")

if __name__ == "__main__":
    graph = ShoppingAssistantGraph()

    # Pilih mode chatbot: invoke atau stream
    print("=" * 60)
    mode = input("Pilih mode chatbot (invoke/stream): ").strip().lower()
    print("=" * 60)

    print("🛍️  Selamat datang di Toko Pakaian Purwadhika!")
    print("   Ketik 'quit' / 'exit' / 'q' untuk keluar.")
    print("=" * 60)
    if mode == "stream":
        chatbot_stream(graph)
    else:
        chatbot(graph)


