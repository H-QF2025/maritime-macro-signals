def freight_momentum(df):
    df['momentum_30d'] = df['rate'].pct_change(30)
    df['momentum_90d'] = df['rate'].pct_change(90)
    return df