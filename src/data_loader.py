
import pandas as pd

def load_excel_sheets(sheet_dict):

    frames = []

    for sheet_name, df in sheet_dict.items():

        df = df.copy()

        if "Content" not in df.columns:
            continue

        df["source_sheet"] = sheet_name

        df = df[["Platform","Author","Content","Date","source_sheet"]]

        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)

    combined = combined.dropna(subset=["Content"])

    combined = combined.drop_duplicates(subset=["Content"])

    combined = combined.reset_index(drop=True)

    combined["id"] = combined.index

    combined.rename(columns={"Content":"post_snippet"}, inplace=True)

    return combined
