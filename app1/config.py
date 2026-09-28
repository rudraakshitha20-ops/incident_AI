import os
from dotenv import load_dotenv

load_dotenv()

HINDSIGHT_BASE_URL = os.getenv(
    "HINDSIGHT_BASE_URL"
)

HINDSIGHT_API_KEY = os.getenv(
    "hsk_8017ade86e75ef5e2e61741205e77384_974ff8d58a5f169d"
)

HINDSIGHT_BANK_ID = os.getenv(
    "HINDSIGHT_BANK_ID",
    "incident-ai"
)