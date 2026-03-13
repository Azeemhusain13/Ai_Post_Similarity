
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_filter(texts, top_n=50):

    vectorizer = TfidfVectorizer(max_features=5000)

    X = vectorizer.fit_transform(texts)

    sim_matrix = cosine_similarity(X)

    candidates = {}

    for i in range(len(texts)):

        sims = list(enumerate(sim_matrix[i]))

        sims = sorted(sims, key=lambda x: x[1], reverse=True)

        candidates[i] = [idx for idx,score in sims[1:top_n]]

    return candidates
