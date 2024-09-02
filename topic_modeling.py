from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def extract_topics(reviews: List[str], num_topics: int = 5) -> List[List[str]]:
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(reviews)
    
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=0)
    lda.fit(X)
    
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    for topic_idx, topic in enumerate(lda.components_):
        topic_words = [feature_names[i] for i in topic.argsort()[:-11:-1]]
        topics.append(topic_words)
    
    return topics
