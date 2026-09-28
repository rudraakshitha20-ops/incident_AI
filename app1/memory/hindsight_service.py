from hindsight_client import Hindsight

from app1.config import (
    HINDSIGHT_BASE_URL,
    HINDSIGHT_API_KEY,
    HINDSIGHT_BANK_ID
)


class HindsightService:

    def __init__(self):

        self.bank_id = HINDSIGHT_BANK_ID

        self.client = Hindsight(
            base_url=HINDSIGHT_BASE_URL,
            api_key=HINDSIGHT_API_KEY
        )

    def retain(self, content, context=None, metadata=None):

        return self.client.retain(
            bank_id=self.bank_id,
            content=content,
            context=context,
            metadata=metadata
        )

    def recall(self, query):

        return self.client.recall(
            bank_id=self.bank_id,
            query=query,
            max_tokens=4096,
            budget="mid"
        )

    def close(self):

        self.client.close()