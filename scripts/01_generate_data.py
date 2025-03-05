import pandas as pd
import numpy as np
import random
from scipy.spatial.distance import cdist

random.seed(42)
np.random.seed(42)

warehouses = pd.DataFrame({
    'id': ['W1', 'W2', 'W3'],
    'latitude': [48.8566 + random.uniform(-0.1, 0.1) for _ in range(3)],
    'longitude': [2.3522 + random.uniform(-0.1, 0.1) for _ in range(3)],
    'capacity': [500, 400, 300]
})

stores = pd.DataFrame({
    'id': ['S'+str(i) for i in range(1, 11)],
    'latitude': [48.8566 + random.uniform(-0.2, 0.2) for _ in range(10)],
    'longitude': [2.3522 + random.uniform(-0.2, 0.2) for _ in range(10)],
    'demand': [random.randint(20, 80) for _ in range(10)]
})

cost_matrix = cdist(
    warehouses[['latitude', 'longitude']],
    stores[['latitude', 'longitude']],
    metric='euclidean'
)
cost_matrix = pd.DataFrame(cost_matrix, columns=stores['id'], index=warehouses['id'])

warehouses.to_csv('data/raw/warehouses.csv', index=False)
stores.to_csv('data/raw/stores.csv', index=False)
cost_matrix.to_csv('data/processed/cost_matrix.csv')
