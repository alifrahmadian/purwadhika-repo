from typing import Literal
from langgraph.graph import StateGraph,START,END
from .nodes import *
from .state import State

def classify_flow(state: State) -> Literal["product_agent", "promo_agent", "basic_agent"]:
    """
    Fungsi routing: membaca output filter agent dan menentukan node mana yang akan dijalankan selanjutnya.
    Return type harus berupa string yang valid.
    """
    classification = state["messages"][-1].content.strip().lower()
    if classification == "product":
        return "product_agent"
    elif classification == "promo":
        return "promo_agent"
    else:
        return "basic_agent"

class ShoppingAssistantGraph(StateGraph):
    def __init__(self):
        super().__init__(State)
        self.add_node("filter_agent", filter_agent)
        self.add_node("product_agent", product_agent)
        self.add_node("promo_agent", promo_agent)
        self.add_node("basic_agent", basic_agent)
        self.add_edge(START, "filter_agent")
        self.add_conditional_edges("filter_agent", classify_flow)
        self.add_edge("product_agent", END)
        self.add_edge("promo_agent", END)
        self.add_edge("basic_agent", END)
    

# Buat test untuk memastikan workflow berjalan dengan benar
if __name__ == "__main__":
    graph = ShoppingAssistantGraph()
    app = graph.compile()

    result = app.invoke({
        "messages": [
            {"role": "user", "content": "ada promo apa?"}
        ],
        "history": [],
    })

    print(result["messages"][-1].content)
    