from statsmodels.tsa.api import VAR

def train_var(df):
    model = VAR(df)
    results = model.fit(4)
    return results