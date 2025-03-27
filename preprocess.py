import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les fichiers
file_data = "./data/CWB_2021.csv"


# Charger le fichier principal
df_data = pd.read_csv(file_data, encoding="latin1")

# Afficher les premières lignes et les informations générales
df_data.info(), df_data.head()


# Vérifier les valeurs manquantes
missing_values = df_data.isnull().sum()

# Statistiques descriptives des variables numériques
summary_statistics = df_data.describe()

# Visualisation des valeurs manquantes
plt.figure(figsize=(10, 5))
sns.heatmap(df_data.isnull(), cmap="viridis", cbar=False, yticklabels=False)
plt.title("Carte des valeurs manquantes")
plt.show()

# Afficher les résultats
missing_values, summary_statistics