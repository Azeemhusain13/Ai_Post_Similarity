
import pandas as pd
from .data_loader import load_excel_sheets
from .preprocessing import preprocess
from .stage1_filter import tfidf_filter
from .embedding_rerank import semantic_rerank
from .clustering import cluster_posts, generate_cluster_titles

def run_pipeline(sheet_dict,top_k=5,threshold=0.5):

    df = load_excel_sheets(sheet_dict)

    df = preprocess(df)

    candidates = tfidf_filter(df["clean_text"].tolist())

    results,embeddings = semantic_rerank(df,candidates,top_k)

    result_df = pd.DataFrame(results)

    result_df = result_df[
        result_df["similarity_score"] >= threshold
    ]

    df = cluster_posts(df,embeddings)

    df = generate_cluster_titles(df)

    result_df = result_df.merge(
        df[["id","cluster","cluster_title"]],
        left_on="source_id",
        right_on="id",
        how="left"
    )

    return result_df
