import os
from typing import List
from dotenv import load_dotenv
from pydantic_ai import Agent, RunContext
from pydantic_ai.models import ModelMessage
from pydantic import BaseModel, Field

load_dotenv()

class ChatAgentDeps(BaseModel):
  username: str | None = Field(None, description="User's name if logged in.")

chat_agent = Agent(
  os.getenv("OPENAI_MODEL"),
  deps_type=ChatAgentDeps,
  output_type=str,
)

@chat_agent.tool
async def get_current_date_time(ctx: RunContext[ChatAgentDeps]) -> str:
  """Get the current date and time."""
  from datetime import datetime
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@chat_agent.tool
async def get_user_name(ctx: RunContext[ChatAgentDeps]) -> str:
  """Get the user's name if user is logged in (Google)."""
  return ctx.deps.username or "User is not logged in."

class ChatAgent():
  def __init__(self):
    self.message_history : List[ModelMessage] = []

  async def chat(self, prompt : str, deps : ChatAgentDeps) -> str:
    response = await chat_agent.run(
      user_prompt=prompt,
      message_history=self.message_history,
      deps=deps
    )

    self.message_history = response.all_messages()

    return response.output or "Sorry, unexpected error occurred."