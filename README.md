# PROJET D'OPTIMISATION DE RÉSEAU DE DISTRIBUTION

## APERÇU

Ce projet vise à optimiser la structure d'un réseau de distribution en minimisant les coûts de transport tout en respectant les contraintes de capacité et de demande. Il utilise des modèles d'optimisation linéaire et des solveurs comme Gurobi.

---

## FONCTIONNALITÉS

### 1. MODÈLE D'OPTIMISATION
- Minimise les coûts de transport.
- Respecte les contraintes de capacité des entrepôts.
- Satisfait les demandes des magasins.

### 2. TECHNOLOGIES UTILISÉES
- **Python** : Pour le traitement des données et la modélisation.
- **Gurobi** : Solveur d'optimisation.
- **Pandas** : Gestion des données.
- **Matplotlib** : Visualisation géographique.

### 3. STRUCTURE DU PROJET
| Dossier/Fichier                         | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| `Supply_Network_Optimization/`         | Dossier racine du projet.                                                   |
| `data/`                                 | Contient les données brutes et traitées.                                    |
| `data/raw/`                             | Contient les données brutes.                                                |
| `data/raw/warehouses.csv`              | Données brutes des entrepôts.                                               |
| `data/raw/stores.csv`                  | Données brutes des magasins.                                                |
| `data/processed/`                       | Contient les données traitées.                                              |
| `data/processed/cost_matrix.csv`       | Matrice des coûts générée.                                                  |
| `results/`                              | Contient les résultats du modèle et les cartes.                             |
| `results/optimal_results.csv`           | Résultats du modèle d'optimisation.                                         |
| `results/maps/`                         | Contient les cartes générées.                                               |
| `results/maps/optimal_routes.png`      | Carte du réseau optimisé.                                                  |
| `scripts/`                              | Contient les scripts Python pour le projet.                                 |
| `scripts/01_generate_data.py`           | Script pour générer des données simulées.                                   |
| `scripts/02_optimization_model.py`      | Script pour le modèle d'optimisation.                                       |
| `scripts/03_visualization.py`           | Script pour la visualisation avec Matplotlib.                               |
| `README.md`                             | Instructions de démarrage et documentation du projet.                       |

---




# INSTRUCTIONS D'INSTALLATION


## Visualisation géographique avec QGIS

Pour une visualisation géographique plus détaillée, nous utilisons QGIS. Les étapes pour reproduire la carte sont les suivantes :

1. **Téléchargez et installez QGIS** : https://www.qgis.org/fr/site/forusers/download.html
2. **Importez les données** :
   - Entrepôts : `data/raw/warehouses.csv`
   - Magasins : `data/raw/stores.csv`
   - Routes optimales : `results/optimal_results.csv`
3. **Créez une couche de lignes** pour les routes optimales.
4. **Stylisez les couches** avec des symboles distincts pour les entrepôts, les magasins et les routes.
5. **Exportez la carte** en tant qu'image pour l'inclure dans le rapport.

![Carte QGIS](results/maps/optimal_routes_qgis.png)



## Créer un environnement virtuel
   ```bash```
   python3.10 -m venv venv


## Activer l'environnement virtuel


## Installer les dépendances

pip install pandas numpy gurobipy matplotlib



## EXÉCUTION DU PROJET
### Générer les données

python scripts/01_generate_data.py

### Exécuter le modèle d'optimisation

python scripts/02_optimization_model.py

### Générer la carte

python scripts/03_visualization.py


