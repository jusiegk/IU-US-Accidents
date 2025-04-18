import os
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "data/US_Accidents_March23.csv"

if not os.path.exists(csv_path):
    print("❗ CSV-Datei fehlt. Bitte in /data/us_accidents.csv ablegen.")
    exit()

print("🟢 CSV wird geladen...")
df = pd.read_csv(csv_path, nrows=5000)
print(f"✅ CSV geladen: {len(df)} Zeilen")

state_counts = df['State'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(14, 6))
state_counts.plot(kind='bar')
plt.title("Anzahl der Unfälle pro Bundesstaat")
plt.xlabel("Bundesstaat")
plt.ylabel("Unfälle")
plt.tight_layout()
plt.savefig("output/accidents_by_state.png")
print("✅ PNG erfolgreich erzeugt.")

