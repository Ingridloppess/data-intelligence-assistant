import pandas as pd

def clean_dataframe(df):
    df = df.copy()

    df["data"] = pd.to_datetime(
        df["data"],
        dayfirst=True
    )
    df["valor"] = (
        df["valor"]
        .str.replace(",",".")
        .astype(float)
    )
    df = df.sort_values(
        by="data"
    )
    return df