from ingestion.ais_pipeline import load_ais, clean_ais
from routing.route_detection import detect_routes
from signals.freight_momentum import freight_momentum
from models.var_model import train_var

df = load_ais('data/raw/ais.csv')
df = clean_ais(df)

routes = detect_routes(df)
signal = freight_momentum(routes)
model = train_var(signal)

print("Pipeline complete")