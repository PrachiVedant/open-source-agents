from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from backend.llm.manager import LLMManager
from tools.manager import ToolManager


class AgentState(MessagesState):
    agent_config: dict


class AgentGraph:
    def __init__(self, config):
        self.config = config
        self.tools = []
        self.llm_with_tools = None

    def chatbot(self, state: AgentState):
        if self.llm_with_tools is None:
            raise RuntimeError("Graph has not been built yet.")

        response = self.llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}

    async def build(self):
        tool_manager = ToolManager(self.config)
        self.tools = await tool_manager.get_tools()

        llm = LLMManager(self.config).get_llm()
        self.llm_with_tools = llm.bind_tools(self.tools)

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



