import pandas as pd
import glob
import os

# Adapter ce chemin avec ton vrai chemin
dossier_node1 = r"C:\Users\serine\OneDrive\Desktop\stage-IA\dataset\0"

# Lire tous les parquet d'un seul nœud et les combiner
fichiers = glob.glob(os.path.join(dossier_node1, "*.parquet"))
print(f"Fichiers dans node_01 : {len(fichiers)}")

dfs = []
for f in fichiers:
    df = pd.read_parquet(f, engine="pyarrow")
    dfs.append(df)

df_node1 = pd.concat(dfs, ignore_index=True)
df_node1 = df_node1.sort_values('timestamp').reset_index(drop=True)

print(f"Shape node_01 : {df_node1.shape}")
print(f"Période : {df_node1['timestamp'].min()} → {df_node1['timestamp'].max()}")
print(f"Colonnes : {df_node1.columns.tolist()}")