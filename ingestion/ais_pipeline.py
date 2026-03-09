import pandas as pd

def load_ais(filepath):
    df = pd.read_csv(filepath)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

def clean_ais(df):
    df = df.dropna(subset=["lat","lon"])
    df = df.sort_values("timestamp")
    return df