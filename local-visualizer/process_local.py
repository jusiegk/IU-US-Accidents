import os
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "../data/us_accidents.csv"

if not os.path.exists(csv_path):
    print("❗ CSV-Datei fehlt. Bitte unter /data/us_accidents.csv ablegen.")
    exit()

print("🟢 CSV wird geladen...")
df = pd.read_csv(csv_path, nrows=10000)
print(f"✅ CSV geladen: {len(df)} Zeilen")

state_counts = df['State'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
state_counts.plot(kind='bar')
plt.title("Anzahl der Unfälle pro Bundesstaat")
plt.xlabel("Bundesstaat")
plt.ylabel("Unfälle")
plt.tight_layout()

output_path = "../output/accidents_by_state.png"
plt.savefig(output_path)
print(f"✅ PNG gespeichert unter: {output_path}")

