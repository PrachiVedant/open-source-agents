from typing import Annotated

from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages

from backend.llm.manager import LLMManager
from tools.manager import ToolManager


class AgentState(MessagesState):
    agent_config: dict


class AgentGraph:
    def __init__(self, config):
        self.config = config
        self.llm = LLMManager(config).get_llm()
        self.tools = ToolManager(config).get_tools()
        self.llm_with_tools = self.llm.bind_tools(self.tools)

    def chatbot(self, state: AgentState):
        response = self.llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}

    def build(self):
        builder = StateGraph(AgentState)

        builder.add_node("chatbot", self.chatbot)
        builder.add_node("tools", ToolNode(self.tools))
        builder.add_edge(START, "chatbot")
        builder.add_conditional_edges(
            "chatbot",
            tools_condition,
        )
        builder.add_edge("tools", "chatbot")
        builder.add_edge("chatbot", END)

        return builder.compile()



