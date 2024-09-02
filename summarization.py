from transformers import BartTokenizer, pipeline
from typing import List

# Initialize the tokenizer
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

def chunk_text(text: str, max_length: int = 1024) -> List[str]:
    # Tokenize the text
    tokens = tokenizer.encode(text, truncation=False)
    chunks = []

    while len(tokens) > max_length:
        chunk_tokens = tokens[:max_length]
        chunk = tokenizer.decode(chunk_tokens, skip_special_tokens=True)
        chunks.append(chunk)
        tokens = tokens[max_length:]

    if tokens:
        chunk = tokenizer.decode(tokens, skip_special_tokens=True)
        chunks.append(chunk)

    return chunks

# Initialize the summarization pipeline with the BART model
SUMMARIZER = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_reviews(reviews: List[str]) -> str:
    concatenated_reviews = " ".join(reviews)
    chunks = chunk_text(concatenated_reviews, max_length=1024)

    summaries = []
    for chunk in chunks:
        try:
            summary = SUMMARIZER(chunk, max_length=150, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        except Exception as e:
            print(f"Error summarizing text chunk: {e}")
            #summaries.append("Error summarizing text")

    return " ".join(summaries)






































# from typing import List
# from transformers import pipeline

# def summarize_reviews(reviews: List[str]) -> str:
#     summarizer = pipeline("summarization")
#     concatenated_reviews = " ".join(reviews)
#     summary = summarizer(concatenated_reviews, max_length=150, min_length=30, do_sample=False)
#     return summary[0]['summary_text']
