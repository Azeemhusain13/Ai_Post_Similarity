
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

def semantic_rerank(df,candidates,top_k=5):

    texts = df["clean_text"].tolist()

    embeddings = model.encode(texts,batch_size=32)

    results = []

    for i in range(len(texts)):

        source_vec = embeddings[i]

        candidate_ids = candidates[i]

        candidate_vecs = embeddings[candidate_ids]

        sims = cosine_similarity(
            [source_vec],
            candidate_vecs
        )[0]

        ranked = sorted(
            zip(candidate_ids,sims),
            key=lambda x:x[1],
            reverse=True
        )

        for cid,score in ranked[:top_k]:

            results.append({

                "source_id":df.iloc[i]["id"],
                "source_post_snippet":df.iloc[i]["post_snippet"],
                "matched_id":df.iloc[cid]["id"],
                "matched_post_snippet":df.iloc[cid]["post_snippet"],
                "similarity_score":float(score)

            })

    return results, embeddings
