import os
from typing import List
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models import ModelMessage

load_dotenv()

class ChatAgent():
  def __init__(self):
    self.model : str = os.getenv("OPENAI_MODEL")
    self.api_key : str = os.getenv("OPENAI_API_KEY")
    self.message_history : List[ModelMessage] = []

  async def chat(self, prompt : str) -> str:
    agent = Agent(self.model)

    response = await agent.run(
      user_prompt=prompt,
      message_history=self.message_history
    )

    self.message_history = response.all_messages()

    return response.output or "Sorry, unexpected error occurred."