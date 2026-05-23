import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = os.getenv("AUDIT_MODEL", "gpt-4")
MAX_FILE_SIZE_KB = int(os.getenv("MAX_FILE_SIZE_KB", "500"))

if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY is not set. Add it to your .env file.")
