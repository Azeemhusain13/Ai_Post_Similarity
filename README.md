# AI Post Similarity Matching & Topic Clustering (Live)

This project builds an AI pipeline to identify **similar posts** and group them into **topic clusters** using semantic embeddings and vector similarity search.

The system processes Excel files containing social media posts, identifies semantically similar content, and organizes them into clusters with topic summaries.

---

# Features

- Multi-sheet Excel ingestion
- Automatic column detection (author + post text)
- Text preprocessing
- Sentence embeddings using **MiniLM**
- Vector similarity search using **FAISS**
- Hybrid similarity scoring (Semantic + Fuzzy matching)
- Graph-based clustering of similar posts
- Cluster topic generation
- Interactive **Streamlit UI**
- Downloadable CSV outputs

---

# Project Structure
# AI Post Similarity Matching & Topic Clustering

This project builds an AI pipeline to identify **similar posts** and group them into **topic clusters** using semantic embeddings and vector similarity search.

The system processes Excel files containing social media posts, identifies semantically similar content, and organizes them into clusters with topic summaries.

---

# Features

- Multi-sheet Excel ingestion
- Automatic column detection (author + post text)
- Text preprocessing
- Sentence embeddings using **MiniLM**
- Vector similarity search using **FAISS**
- Hybrid similarity scoring (Semantic + Fuzzy matching)
- Graph-based clustering of similar posts
- Cluster topic generation
- Interactive **Streamlit UI**
- Downloadable CSV outputs

---

# Project Structure
AI_Post_Similarity/
│
├── app.py
├── requirements.txt
├── README.md
│
└── src/
├── pipeline.py
├── data_loader.py
├── preprocessing.py
├── stage1_filter.py
├── embedding_rerank.py
└── clustering.py



# Installation

##Clone the Repository

```bash
git clone https://github.com/AzeemHusain13/AI_Post_Similarity.git
cd AI_Post_Similarity


pip install -r requirements.txt

streamlit run app.py


**How the Pipeline Works**

1️⃣ Upload an Excel file with posts
2️⃣ System detects author and post text columns automatically
3️⃣ Text preprocessing and cleaning
4️⃣ Generate embeddings using MiniLM transformer
5️⃣ Similarity search using FAISS vector index
6️⃣ Hybrid scoring with semantic + fuzzy similarity
7️⃣ Graph-based clustering of related posts
8️⃣ Cluster titles generated from the most frequent keywords

**Output**

The application generates three outputs:

Output File	Description
similarity_results.csv	Pairwise similarity results
cluster_posts.csv	All posts grouped by cluster
cluster_summary.csv	Cluster-level summary

-----------------------

Technologies Used

Python
Streamlit
PyTorch
HuggingFace Transformers
FAISS
RapidFuzz
Pandas
NumPy

-----------------------
##Author

Azeem Husain Khan

GitHub: https://github.com/Azeemhusain13
LinkedIn: https://www.linkedin.com/in/azeem-husain-khan-129a041b5/
