from qdrant_client import QdrantClient, models
import os
from dotenv import load_dotenv

load_dotenv()

class VectorDB():
  def __init__(self):
    self.client = QdrantClient(
      url=os.getenv("QDRANT_URL"), 
      api_key=os.getenv("QDRANT_API_KEY"),
    )

  def create_collection(self, collection_name, vector_size) -> bool:
    success = self.client.recreate_collection(
      collection_name=collection_name,
      vectors_config=models.VectorParams(
        size=vector_size,
        distance=models.Distance.COSINE,
      )
    )
    return success

  def get_collections(self):
    return self.client.get_collections()
