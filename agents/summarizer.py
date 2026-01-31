import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

class SummarizerAgent:
    def __init__(self):
        self.token = os.getenv("HUGGINGFACE_API_TOKEN")
        self.summarizer = None  # lazy init

    def _load_model(self):
        if self.summarizer is None:
            self.summarizer = pipeline(
                task="summarization",
                model="sshleifer/distilbart-cnn-12-6",  # IMPORTANT (lighter)
                use_auth_token=self.token
            )

    def chunk_text(self, text, chunk_size=800):
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    def summarize(self, text):
        self._load_model()  # load only when needed

        chunks = self.chunk_text(text)
        summaries = []

        for chunk in chunks[:2]:  # keep small for cloud
            result = self.summarizer(
                chunk,
                max_length=120,
                min_length=40,
                do_sample=False
            )
            summaries.append(result[0]["summary_text"])

        return " ".join(summaries)
