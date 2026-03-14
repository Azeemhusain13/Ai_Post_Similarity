import pandas as pd
import faiss

from src.stage1_filter import hybrid_similarity
from src.clustering import cluster_posts, generate_cluster_title


def run_pipeline(posts, embeddings, df, author_col, top_k=5):

    faiss.normalize_L2(embeddings)

    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)

    index.add(embeddings)

    distances, indices = index.search(embeddings, top_k + 1)

    similarity_results = []

    for i in range(len(posts)):

        for j in range(1, top_k + 1):

            idx = indices[i][j]

            embedding_score = float(distances[i][j])

            final_score = hybrid_similarity(
                posts[i],
                posts[idx],
                embedding_score
            )

            similarity_results.append({

                "source_id": i,
                "source_post": posts[i],
                "matched_id": idx,
                "matched_post": posts[idx],
                "embedding_score": embedding_score,
                "final_similarity_score": final_score

            })

    similarity_df = pd.DataFrame(similarity_results)

    clusters = cluster_posts(similarity_df, posts)

    cluster_data = []
    cluster_summary = []

    for cluster_id, cluster in enumerate(clusters):

        texts = [posts[i] for i in cluster]

        title = generate_cluster_title(texts)

        authors = (
            df.iloc[cluster][author_col].astype(str).tolist()
            if author_col else []
        )

        for idx in cluster:

            cluster_data.append({

                "cluster_id": cluster_id,
                "cluster_title": title,
                "author": df.iloc[idx][author_col] if author_col else str(idx),
                "post_snippet": posts[idx],
                "sheet_name": df.iloc[idx]["sheet_name"]

            })

        cluster_summary.append({

            "cluster_id": cluster_id,
            "cluster_title": title,
            "grouped_authors": ", ".join(sorted(set(authors))),
            "num_posts": len(cluster)

        })

    cluster_df = pd.DataFrame(cluster_data)
    cluster_summary_df = pd.DataFrame(cluster_summary)

    return similarity_df, cluster_df, cluster_summary_df