
from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer

def cluster_posts(df,embeddings):

    clustering = DBSCAN(
        eps=0.5,
        min_samples=2,
        metric="cosine"
    ).fit(embeddings)

    df["cluster"] = clustering.labels_

    return df


def generate_cluster_titles(df):

    titles = {}

    for cluster in df["cluster"].unique():

        if cluster == -1:
            continue

        texts = df[df["cluster"]==cluster]["clean_text"]

        vectorizer = TfidfVectorizer(max_features=5)

        X = vectorizer.fit_transform(texts)

        words = vectorizer.get_feature_names_out()

        titles[cluster] = " ".join(words)

    df["cluster_title"] = df["cluster"].map(titles)

    return df
