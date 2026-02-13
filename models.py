from enum import Enum
from typing import Annotated
from pydantic import AfterValidator, BaseModel, Field, StringConstraints, field_validator


class StatusType(str, Enum):
  DONE = "hecho"
  PENDING = "pending"

class Category(BaseModel):
  id: int
  name: str

class User(BaseModel):
  id: int
  name: str
  username:str

def validar_espacios_y_max(value: str) -> str: 
  if value.strip() == "": 
    raise ValueError("El campo no debe contener solo espacios") 
  if len(value.strip()) > 20: 
    raise ValueError("Máximo 20 caracteres") 
  return value

class Task(BaseModel):
  id:int =  Field(gt=0)
  name:  Annotated[str, AfterValidator(validar_espacios_y_max )]  = Field(min_length=3)
  description:   Annotated[str, AfterValidator(validar_espacios_y_max)] = Field(min_length=3)
  status: StatusType 

  #@field_validator('description', mode='after')
  #@classmethod
  #def is_even(cls, value: str) -> str:
  #      if value.strip()== "" :
  #          raise ValueError(f'La description no debe contener espacios vacios')
  #      return value  
