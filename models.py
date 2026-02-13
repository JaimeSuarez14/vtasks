from enum import Enum
from pydantic import BaseModel


class StatusType(str, Enum):
  DONE = "hecho"
  PENDING = "pending"

class Task(BaseModel):
  id:int
  name: str
  description: str
  status: StatusType