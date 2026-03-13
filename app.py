import streamlit as st
import pandas as pd
from src.pipeline import run_pipeline

st.set_page_config(
    page_title="AI Post Similarity & Clustering",
    layout="wide"
)

st.title("AI Post Similarity & Clustering System")

st.markdown(
"""
Upload an Excel file containing social media posts.  
The system will:

• Identify similar posts  
• Compute similarity scores  
• Cluster posts into topics  
• Generate cluster titles
"""
)

# Sidebar configuration
st.sidebar.header("Configuration")

top_k = st.sidebar.slider(
    "Top Similar Matches",
    min_value=1,
    max_value=10,
    value=5
)

threshold = st.sidebar.slider(
    "Similarity Threshold",
    min_value=0.0,
    max_value=1.0,
    value=0.5
)

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file:

    try:

        st.subheader("Dataset Preview")

        excel_data = pd.read_excel(uploaded_file, sheet_name=None)

        first_sheet = list(excel_data.keys())[0]

        st.dataframe(excel_data[first_sheet].head())

        if st.button("Run Similarity Analysis"):

            with st.spinner("Processing dataset..."):

                result = run_pipeline(
                    excel_data,
                    top_k=top_k,
                    threshold=threshold
                )

            st.success("Analysis Completed")

            st.subheader("Similarity Results")

            st.dataframe(result.head(50))

            csv = result.to_csv(index=False)

            st.download_button(
                label="Download Results CSV",
                data=csv,
                file_name="similar_posts_results.csv",
                mime="text/csv"
            )

    except Exception as e:

        st.error(f"Error processing file: {str(e)}")

else:

    st.info("Please upload an Excel file to begin analysis.")
