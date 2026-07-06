from langgraph.graph import MessagesState


class AgentState(MessagesState):
    agent_config: dict
