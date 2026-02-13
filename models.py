from enum import Enum
from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints, field_validator


class StatusType(str, Enum):
  DONE = "hecho"
  PENDING = "pending"

class Task(BaseModel):
  id:int =  Field(gt=0)
  name: str  = Field(min_length=3, strip_whitespace=True)
  description:  str = Field(min_length=3)
  status: StatusType 

  @field_validator('description', mode='after')  
  @classmethod
  def is_even(cls, value: str) -> str:
        if value.strip()==0 :
            raise ValueError(f'{value} nos debe contener espacios vacios')
        return value  
