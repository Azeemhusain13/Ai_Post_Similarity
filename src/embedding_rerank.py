import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel

torch.set_num_threads(1)
torch.set_num_interop_threads(1)


def load_model():

    tokenizer = AutoTokenizer.from_pretrained(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    model = AutoModel.from_pretrained(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    return tokenizer, model


def embed(texts, tokenizer, model):

    batch_size = 32
    all_embeddings = []

    for i in range(0, len(texts), batch_size):

        batch = texts[i:i + batch_size]

        inputs = tokenizer(
            batch,
            padding=True,
            truncation=True,
            return_tensors="pt"
        )

        with torch.no_grad():
            outputs = model(**inputs)

        emb = outputs.last_hidden_state.mean(dim=1)

        all_embeddings.append(emb.numpy())

    return np.vstack(all_embeddings).astype("float32")