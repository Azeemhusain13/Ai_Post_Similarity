import pandas as pd


def load_excel(file):

    xls = pd.ExcelFile(file)

    dfs = []

    for sheet in xls.sheet_names:

        df = pd.read_excel(
            file,
            sheet_name=sheet,
            header=1
        )

        df["sheet_name"] = sheet

        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)

    return df