from rapidfuzz import fuzz


def hybrid_similarity(text1, text2, embedding_score):

    fuzzy_score = fuzz.partial_ratio(text1, text2) / 100

    return (0.7 * embedding_score) + (0.3 * fuzzy_score)