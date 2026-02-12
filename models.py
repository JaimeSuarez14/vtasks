from enum import Enum


class StatusType(str, Enum):
  DONE = "hecho"
  PENDING = "pending"