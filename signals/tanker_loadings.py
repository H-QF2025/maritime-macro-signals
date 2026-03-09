def tanker_loadings(df):
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    loadings = df.groupby('port')['vessel_id'].count()
    signal = loadings.pct_change()
    return signal