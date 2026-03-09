def congestion_index(df):
    waiting = df[df['speed'] < 1]
    congestion = waiting.groupby('port')['vessel_id'].count()
    return congestion