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
        # Guard against empty / tiny text
        if not text or len(text.strip()) < 50:
            return "No actionable items found."

        self._load_model()  # load only when needed

        prompt = (
            "Extract action items or tasks from the following text:\n\n"
            f"{text}"
        )

        # Dynamically adjust generation length
        input_len = len(prompt.split())

        max_len = min(120, max(30, input_len // 2))
        min_len = min(40, max(10, input_len // 4))

        result = self.extractor(
            prompt,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )

        return result[0]["summary_text"]
