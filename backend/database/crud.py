from backend.database.connection import SessionLocal
from backend.database.models import Agent


class AgentRepository:
    def create(self,name,description,config):
        db=SessionLocal()
        try:
            agent=Agent(
                name=name,
                description=description,
                config=config
            )
            db.add(agent)
            db.commit()
            db.refresh(agent)
            return agent
        finally:
            db.close()
    
    def list(self):
        db=SessionLocal()
        try:
            return db.query(Agent).all()
        finally:
            db.close()
    
    def get(self,agent_id):
        db=SessionLocal()
        try:
            return db.query(Agent).filter(Agent.id == agent_id).first()
        finally:
            db.close()
    
    def update(self,name,config,description,agent_id):
        db=SessionLocal()
        try:
            agents=(db.query(Agent).filter(Agent.id == agent_id).first())

            if not agents:
                return None
            agents.name=name
            agents.description=description
            agents.config=config

            db.commit()
            db.refresh(agents)
            return agents
        finally:
            db.close()
    
    def delete(self,name,config,description,agent_id):
        db=SessionLocal()
        try:
            agents=(db.query(Agent).filter(Agent.id == agent_id).first())

            if not agents:
                return None
            
            agents.name=name
            agents.description=description
            agents.config=config

            db.delete(agents)
            db.commit()
            return True
        finally:
            db.close()
