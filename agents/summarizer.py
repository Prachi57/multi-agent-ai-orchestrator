import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

class SummarizerAgent:
    def __init__(self):
        self.token = os.getenv("HUGGINGFACE_API_TOKEN")

        self.summarizer = pipeline(
            task="summarization",
            model="facebook/bart-large-cnn",
            use_auth_token=self.token
        )

    def chunk_text(self, text, chunk_size=800):
        chunks = []
        start = 0
        while start < len(text):
            chunks.append(text[start:start + chunk_size])
            start += chunk_size
        return chunks

    def summarize(self, text):
        chunks = self.chunk_text(text)
        summaries = []

        for chunk in chunks[:3]:
            result = self.summarizer(
                chunk,
                max_length=130,
                min_length=50,
                do_sample=False
            )
            summaries.append(result[0]["summary_text"])

        return " ".join(summaries)
