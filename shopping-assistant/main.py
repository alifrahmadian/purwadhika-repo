from graph.workflow import ShoppingAssistantGraph

def chatbot():
    print("=" * 60)
    print("🛍️  Selamat datang di Toko Pakaian Purwadhika!")
    print("   Ketik 'quit' / 'exit' / 'q' untuk keluar.")
    print("=" * 60)

    graph = ShoppingAssistantGraph()
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

if __name__ == "__main__":
    chatbot()