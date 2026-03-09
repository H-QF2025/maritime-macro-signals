import pandas as pd

def detect_routes(df):
    df['prev_lat'] = df['lat'].shift(1)
    df['prev_lon'] = df['lon'].shift(1)
    df['distance'] = ((df['lat'] - df['prev_lat'])**2 + (df['lon'] - df['prev_lon'])**2)**0.5
    df['voyage_id'] = (df['distance'] > 0.5).cumsum()
    return df