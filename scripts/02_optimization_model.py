from gurobipy import Model, GRB
import pandas as pd

# Charger les données
warehouses = pd.read_csv('data/raw/warehouses.csv')
stores = pd.read_csv('data/raw/stores.csv')
cost_matrix = pd.read_csv('data/processed/cost_matrix.csv', index_col=0)

# Initialiser le modèle
mdl = Model('Supply_Network')
x = mdl.addVars(
    warehouses['id'], stores['id'],
    name='flow', lb=0
)

# Fonction objectif
mdl.setObjective(
    sum(cost_matrix.loc[w, s] * x[w, s] for w in warehouses['id'] for s in stores['id']),
    GRB.MINIMIZE
)

# Contraintes
mdl.addConstrs(
    (sum(x[w, s] for s in stores['id']) <= warehouses.loc[warehouses['id'] == w, 'capacity'].values[0]
     for w in warehouses['id']), 'Capacity'
)

mdl.addConstrs(
    (sum(x[w, s] for w in warehouses['id']) >= stores.loc[stores['id'] == s, 'demand'].values[0]
     for s in stores['id']), 'Demand'
)

# Résolution
mdl.optimize()

# Exporter les résultats
if mdl.status == GRB.OPTIMAL:
    results = []
    for w in warehouses['id']:
        for s in stores['id']:
            if x[w, s].X > 0:
                results.append({
                    'warehouse': w,
                    'store': s,
                    'flow': x[w, s].X,
                    'cost': cost_matrix.loc[w, s] * x[w, s].X
                })
    pd.DataFrame(results).to_csv('results/optimal_results.csv', index=False)
    print(f"Coût total optimal : {mdl.objVal:.2f}")
else:
    print("Aucune solution trouvée")