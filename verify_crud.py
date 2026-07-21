from backend.database.crud import AgentRepository

repo = AgentRepository()
agent = repo.create('test-agent', 'created via verification', {'mode': 'test'})
print(agent.id, agent.name)
