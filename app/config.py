from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
STORAGE_BACKEND = os.getenv("STORAGE_BACKEND", "postgres")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
