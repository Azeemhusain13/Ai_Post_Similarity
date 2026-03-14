def cluster_posts(similarity_df, posts, threshold=0.80):

    visited = set()
    clusters = []

    for i in range(len(posts)):

        if i in visited:
            continue

        cluster = {i}
        queue = [i]

        while queue:

            current = queue.pop(0)

            matches = similarity_df[
                (similarity_df["source_id"] == current) &
                (similarity_df["final_similarity_score"] >= threshold)
            ]["matched_id"].tolist()

            for m in matches:

                if m not in cluster:

                    cluster.add(m)
                    queue.append(m)

        visited.update(cluster)
        clusters.append(sorted(list(cluster)))

    return clusters


def generate_cluster_title(posts):

    words = " ".join(posts).split()

    freq = {}

    for w in words:
        freq[w] = freq.get(w, 0) + 1

    top_words = sorted(freq, key=freq.get, reverse=True)[:3]

    return " ".join(top_words)