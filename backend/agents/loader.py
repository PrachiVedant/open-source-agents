import json
from pathlib import Path


class AgentLoader:
    def __init__(self, agent_file_path):
        self.agent_file_path = agent_file_path

    @classmethod
    def load(cls, agent_file_path):
        loader = cls(agent_file_path)
        return loader.load_agents()

    def load_agents(self):
        path = Path(self.agent_file_path)
        if not path.is_absolute():
            base_dir = Path(__file__).resolve().parent.parent
            path = (base_dir / path).resolve()

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)