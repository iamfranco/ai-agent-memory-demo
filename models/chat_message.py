from typing import Literal
from pydantic import BaseModel

def get_avatar(role: str | Literal['user', 'assistant']) -> str:
  if role == 'user': return "👤"
  if role == 'assistant': return "🤖"
  return "❓"

class ChatMessage(BaseModel):
  role: str | Literal['user', 'assistant']
  message: str
