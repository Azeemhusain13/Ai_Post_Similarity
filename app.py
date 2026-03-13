
import streamlit as st
import pandas as pd
from src.pipeline import run_pipeline

st.set_page_config(page_title="AI Post Similarity Finder")

st.title("AI Post Similarity & Clustering")

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx","csv"]
)

top_k = st.slider("Top Matches",1,10,5)

threshold = st.slider(
    "Similarity Threshold",
    0.0,
    1.0,
    0.5
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    st.write("Preview Data")
    st.dataframe(df.head())

    if st.button("Run Similarity Analysis"):

        result = run_pipeline(
            df,
            top_k=top_k,
            threshold=threshold
        )

        st.success("Analysis Complete")

        st.dataframe(result.head(20))

        csv = result.to_csv(index=False)

        st.download_button(
            "Download Results",
            csv,
            "similar_posts.csv"
        )
