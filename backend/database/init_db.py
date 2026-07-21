import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.database.connection import engine
from backend.database.models import Base

Base.metadata.create_all(bind=engine)
print("Database initialized!!")