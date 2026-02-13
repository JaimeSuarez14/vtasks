from enum import Enum
from typing import Annotated
from pydantic import AfterValidator, BaseModel, Field, StringConstraints, field_validator


class StatusType(str, Enum):
  DONE = "hecho"
  PENDING = "pending"

def espacios(value: str) -> str:
    if value.strip()== "":
        raise ValueError(f'{value} is not an even number')
    return value 

class Task(BaseModel):
  id:int =  Field(gt=0)
  name:  Annotated[str, AfterValidator(espacios)]  = Field(min_length=3)
  description:   Annotated[str, AfterValidator(espacios)] = Field(min_length=3)
  status: StatusType 

  #@field_validator('description', mode='after')
  #@classmethod
  #def is_even(cls, value: str) -> str:
  #      if value.strip()== "" :
  #          raise ValueError(f'La description no debe contener espacios vacios')
  #      return value  
