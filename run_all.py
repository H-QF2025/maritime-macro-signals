# run_all.py
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Load and clean AIS data ---
from ingestion.ais_pipeline import load_ais, clean_ais
from routing.route_detection import detect_routes
from signals.freight_momentum import freight_momentum
from signals.tanker_loadings import tanker_loadings
from signals.congestion_index import congestion_index
from models.var_model import train_var

print("Running AIS ingestion...")
df = load_ais("data/raw/ais.csv")
df = clean_ais(df)

# --- 2. Detect shipping routes ---
print("Detecting shipping routes...")
routes = detect_routes(df)

# --- 3. Compute signals ---
print("Computing freight momentum...")
freight_signal = freight_momentum(routes)

print("Computing tanker loadings signal...")
tanker_signal = tanker_loadings(routes)

print("Computing congestion index...")
congestion_signal = congestion_index(routes)

# --- 4. Train VAR model ---
print("Training VAR model...")
var_results = train_var(freight_signal.fillna(0))  # fillna for VAR

# --- 5. Plot all results ---
print("Plotting results...")
plt.figure(figsize=(14,8))

# Freight momentum
plt.subplot(3,1,1)
plt.plot(freight_signal.index, freight_signal.get('momentum_30d', freight_signal.index), 
         label='30-day momentum', marker='o')
plt.plot(freight_signal.index, freight_signal.get('momentum_90d', freight_signal.index), 
         label='90-day momentum', marker='x')
plt.title("Freight Momentum Signals")
plt.ylabel("Momentum")
plt.legend()
plt.grid(True)

# Tanker loadings
plt.subplot(3,1,2)
plt.plot(tanker_signal.index, tanker_signal.values, label='Tanker Loadings', color='orange', marker='o')
plt.title("Tanker Loadings Signal")
plt.ylabel("Loadings")
plt.legend()
plt.grid(True)

# Congestion index
plt.subplot(3,1,3)
plt.plot(congestion_signal.index, congestion_signal.values, label='Congestion Index', color='red', marker='o')
plt.title("Port Congestion Index")
plt.ylabel("Congestion")
plt.legend()
plt.grid(True)

plt.xlabel("Date / Voyage ID")
plt.tight_layout()
plt.show()

print("All tasks complete!")
