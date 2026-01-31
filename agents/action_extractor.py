import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

class ActionExtractorAgent:
    def __init__(self):
        self.token = os.getenv("HUGGINGFACE_API_TOKEN")
        self.extractor = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            token=self.token
        )

    def extract_actions(self, text):
        prompt = (
            "Extract action items or tasks from the following text:\n\n"
            f"{text}"
        )

        result = self.extractor(prompt, max_length=120, min_length=40, do_sample=False)
        return result[0]["summary_text"]
