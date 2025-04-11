from pydantic import BaseModel
from typing import Dict
#creating the schema for our agents and missions

class User(BaseModel):
    username: str
    password: str

class Mission(BaseModel):
    agent_id: str
    mission: str
    details: Dict[str, str]
