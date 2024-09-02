from typing import List
from transformers import pipeline

def summarize_reviews(reviews: List[str]) -> str:
    summarizer = pipeline("summarization")
    concatenated_reviews = " ".join(reviews)
    summary = summarizer(concatenated_reviews, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']
