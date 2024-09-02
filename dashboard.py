import streamlit as st
from scrape_reviews import get_amazon_reviews, translate_text
from sentiment_analysis import analyze_sentiments  # Ensure this module exists and works
from topic_modeling import extract_topics  # Ensure this module exists and works
from summarization import summarize_reviews

st.title('AI-Powered Review Summarization')

url = st.text_input('Enter Amazon Product URL:')
if url:
    with st.spinner('Fetching and processing reviews...'):
        reviews = get_amazon_reviews(url)
        
        if not reviews:
            st.write("No reviews found or there was an error fetching reviews.")
        else:
            # Translate reviews if needed
            translated_reviews = [translate_text(review) for review in reviews]
            #st.write("Translated Reviews:", translated_reviews)

            # Sentiment Analysis
            sentiments = analyze_sentiments(translated_reviews)
            st.write("Sentiments:")
            # for sentiment in sentiments:
            #     st.write(f"Translated Review: {translated_reviews[sentiments.index(sentiment)]}")
            #     st.write(f"Sentiment: {sentiment}")

            # Topic Modeling
            num_topics = st.slider('Number of Topics:', min_value=2, max_value=10, value=5)
            topics = extract_topics(translated_reviews, num_topics=num_topics)
           # st.write("Key Topics:")
            # for idx, words in enumerate(topics):
            #     st.write(f"Topic {idx}: {words}")

            # Summarization
            summary = summarize_reviews(translated_reviews)
            st.write("Summary:", summary)




























































# import streamlit as st
# from scrape_reviews import get_amazon_reviews, translate_text
# from sentiment_analysis import analyze_sentiments
# from topic_modeling import extract_topics
# from summarization import summarize_reviews

# st.title('AI-Powered Review Summarization')

# url = st.text_input('Enter Amazon Product URL:')
# if url:
#     with st.spinner('Fetching and processing reviews...'):
#         reviews = get_amazon_reviews(url)
#         st.write("Original Reviews:", reviews)

#         # Translate reviews if needed
#         translated_reviews = [translate_text(review) for review in reviews]
#         st.write("Translated Reviews:", translated_reviews)

#         # Sentiment Analysis
#         sentiments = analyze_sentiments(translated_reviews)
#         st.write("Sentiments:")
#         for sentiment in sentiments:
#             st.write(f"Translated Review: {translated_reviews[sentiments.index(sentiment)]}")
#             st.write(f"Sentiment: {sentiment}")

#         # Topic Modeling
#         num_topics = st.slider('Number of Topics:', min_value=2, max_value=10, value=5)
#         topics = extract_topics(translated_reviews, num_topics=num_topics)
#         st.write("Key Topics:")
#         for idx, words in enumerate(topics):
#             st.write(f"Topic {idx}: {words}")

#         # Summarization
#         summary = summarize_reviews(translated_reviews)
#         st.write("Summary:", summary)
