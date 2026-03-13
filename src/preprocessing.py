
import re

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+","",text)

    text = re.sub(r"@\w+","",text)

    text = re.sub(r"#\w+","",text)

    text = re.sub(r"[^\w\s]"," ",text)

    text = re.sub(r"\s+"," ",text)

    return text.strip()


def preprocess(df):

    df["clean_text"] = df["post_snippet"].apply(clean_text)

    return df
