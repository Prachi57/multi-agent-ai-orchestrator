import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

class SummarizerAgent:
    def __init__(self):
        self.token = os.getenv("HUGGINGFACE_API_TOKEN")
        self.summarizer = None  # lazy load

    def _load_model(self):
        if self.summarizer is None:
            self.summarizer = pipeline(
                task="summarization",
                model="sshleifer/distilbart-cnn-12-6",
                use_auth_token=self.token
            )

    def chunk_text(self, text, chunk_size=800):
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    def summarize(self, text):
        self._load_model()

        if not text or len(text.strip()) < 50:
            return "Document is too short to summarize."

        chunks = self.chunk_text(text)
        summaries = []

        for chunk in chunks[:2]:
            chunk = chunk.strip()
            if len(chunk) < 50:
                continue

            input_len = len(chunk.split())
            max_len = min(120, max(30, input_len // 2))
            min_len = min(40, max(10, input_len // 4))

            result = self.summarizer(
                chunk,
                max_length=max_len,
                min_length=min_len,
                do_sample=False
            )

            summaries.append(result[0]["summary_text"])

        if not summaries:
            return "No meaningful content found to summarize."

        return " ".join(summaries)
