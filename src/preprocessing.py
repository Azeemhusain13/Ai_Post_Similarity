def clean_text(text):

    if not isinstance(text, str):
        return ""

    return text.lower().strip()


def detect_columns(df):

    author_col = None
    text_col = None

    author_candidates = [
        "author", "username", "user", "account", "handle", "profile", "unnamed:1"
    ]

    text_candidates = [
        "post_snippet", "content", "text", "message", "post", "tweet", "unnamed:2"
    ]

    for col in df.columns:

        col_lower = col.lower()

        if any(x in col_lower for x in author_candidates):
            author_col = col

        if any(x in col_lower for x in text_candidates):
            text_col = col

    return author_col, text_col