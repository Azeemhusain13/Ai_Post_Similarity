import streamlit as st
import pandas as pd
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["KMP_INIT_AT_FORK"] = "FALSE"

from src.data_loader import load_excel
from src.preprocessing import detect_columns, clean_text
from src.embedding_rerank import load_model, embed
from src.pipeline import run_pipeline

st.set_page_config(layout="wide")

st.title("AI Post Similarity & Clustering")

tokenizer, model = load_model()

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file:

    df = load_excel(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    author_col, text_col = detect_columns(df)

    st.subheader("Detected Columns")

    st.write({
        "author_column": author_col,
        "post_text_column": text_col
    })

    if text_col is None:
        st.error("Post text column could not be detected.")
        st.stop()

    posts = df[text_col].astype(str).apply(clean_text).tolist()

    # --------------------------------------------------
    # Top K Slider
    # --------------------------------------------------

    top_k = st.slider(
        "Top Similar Posts",
        1,
        10,
        5
    )

    run_analysis = st.button("Run Analysis")

    if run_analysis:

        # --------------------------------------------------
        # Progress Bar
        # --------------------------------------------------

        progress = st.progress(0)

        with st.spinner("Generating embeddings..."):
            embeddings = embed(posts, tokenizer, model)

        progress.progress(40)

        with st.spinner("Running similarity pipeline..."):

            similarity_df, cluster_df, cluster_summary_df = run_pipeline(
                posts,
                embeddings,
                df,
                author_col,
                top_k
            )

        progress.progress(100)

        # --------------------------------------------------
        # Store results
        # --------------------------------------------------

        st.session_state["similarity_df"] = similarity_df
        st.session_state["cluster_df"] = cluster_df
        st.session_state["cluster_summary_df"] = cluster_summary_df


# --------------------------------------------------
# Show results
# --------------------------------------------------

if "similarity_df" in st.session_state:

    st.subheader("Similarity Results")
    st.dataframe(st.session_state["similarity_df"].head(20))

    st.subheader("Clustered Posts")
    st.dataframe(st.session_state["cluster_df"].head(20))

    st.subheader("Cluster Summary")
    st.dataframe(st.session_state["cluster_summary_df"].head())

    # --------------------------------------------------
    # Download Buttons
    # --------------------------------------------------

    similarity_csv = st.session_state["similarity_df"].to_csv(index=False).encode("utf-8")
    cluster_csv = st.session_state["cluster_df"].to_csv(index=False).encode("utf-8")
    summary_csv = st.session_state["cluster_summary_df"].to_csv(index=False).encode("utf-8")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            "Download Similarity Results",
            similarity_csv,
            file_name="similarity_results.csv",
            mime="text/csv"
        )

    with col2:
        st.download_button(
            "Download Cluster Posts",
            cluster_csv,
            file_name="cluster_posts.csv",
            mime="text/csv"
        )

    with col3:
        st.download_button(
            "Download Cluster Summary",
            summary_csv,
            file_name="cluster_summary.csv",
            mime="text/csv"
        )