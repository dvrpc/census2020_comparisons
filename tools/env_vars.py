import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

DATABASE_URL = os.environ.get("DATABASE_URL")
GDRIVE_PROJECT_ROOT = os.environ.get("GDRIVE_PROJECT_ROOT")
