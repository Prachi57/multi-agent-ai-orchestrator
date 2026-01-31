import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

class ActionExtractorAgent:
    def __init__(self):
        self.token = os.getenv("HUGGINGFACE_API_TOKEN")
        self.extractor = None  # lazy load

    def _load_model(self):
        if self.extractor is None:
            self.extractor = pipeline(
                task="summarization",
                model="sshleifer/distilbart-cnn-12-6",  # lighter model
                use_auth_token=self.token
            )

    def extract_actions(self, text):
        self._load_model()  # load only when needed

        prompt = (
            "Extract action items or tasks from the following text:\n\n"
            f"{text}"
        )

        result = self.extractor(
            prompt,
            max_length=120,
            min_length=40,
            do_sample=False
        )

        return result[0]["summary_text"]
