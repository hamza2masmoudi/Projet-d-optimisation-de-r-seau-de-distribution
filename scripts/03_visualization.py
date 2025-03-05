import matplotlib.pyplot as plt
import pandas as pd

# Charger les données
results = pd.read_csv('results/optimal_results.csv')
warehouses = pd.read_csv('data/raw/warehouses.csv')
stores = pd.read_csv('data/raw/stores.csv')

# Créer la figure
plt.figure(figsize=(12, 8))

# Dessiner les lignes de livraison
for _, row in results.iterrows():
    w = warehouses[warehouses['id'] == row['warehouse']]
    s = stores[stores['id'] == row['store']]
    plt.plot(
        [w['longitude'].values[0], s['longitude'].values[0]],
        [w['latitude'].values[0], s['latitude'].values[0]],
        'b-', alpha=0.7
    )

# Dessiner les entrepôts et magasins
plt.scatter(
    warehouses['longitude'], warehouses['latitude'],
    c='red', s=100, label='Entrepôts'
)
plt.scatter(
    stores['longitude'], stores['latitude'],
    c='green', s=50, label='Magasins'
)

# Personnaliser la figure
plt.legend()
plt.title("Réseau de distribution optimisé")

# Sauvegarder la figure dans results/maps/
plt.savefig('results/maps/optimal_routes.png')
plt.close()