import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "ollama/qwen2.5:14b",
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "nomic-embed-text",
)

VECTOR_DB_DIR = os.getenv(
    "VECTOR_DB_DIR",
    "vector_db",
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "career_docs",
)

DEFAULT_TOP_K = int(
    os.getenv(
        "DEFAULT_TOP_K",
        "5",
    )
)

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434",
)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///career_agent.db",
)

def validate_config():
    return True