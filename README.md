
# Projet d'Optimisation de Portefeuille d'Actions

## Description
Ce projet est consacré à la résolution d’un problème d'optimisation de portefeuille d'actions en utilisant deux approches algorithmique : 

1. **Approche brute-force** (fichier `bruteforce.py`) : Cette méthode teste toutes les combinaisons possibles d’actions pour trouver la solution offrant le meilleur rapport coût/profit, tant que les contraintes budgétaires sont respectées.
2. **Approche à l’aide de l’algorithme du sac à dos** (fichier `optimized.py`) : Une approche optimisée basée sur la programmation dynamique pour résoudre plus efficacement le problème.

Chaque méthode utilise des données issues de fichiers CSV pour effectuer des calculs et retourne la meilleure combinaison d’actions avec leurs bénéfices correspondants.

---

## Fonctionnalités
- Charger des listes d'actions à partir de fichiers CSV.
- Calculer et comparer les performances des combinaisons d’actions.
- Respect des contraintes budgétaires : le portefeuille ne dépasse pas un budget préalablement fixé (500 € par défaut).
- Afficher les résultats optimaux :
  - Meilleure combinaison d’actions.
  - Somme totale investie.
  - Profit total obtenu.
  - Ratio coût/profit.

---

## Configuration requise
### Bibliothèques Python nécessaires :
- **Pandas** : pour manipuler et analyser les données contenues dans les fichiers CSV.
- **itertools** (inclus dans la bibliothèque standard Python) : utilisé dans la méthode brute-force.
- **timeit** (inclus dans la bibliothèque standard Python) : pour mesurer le temps d'exécution.

### Installation des dépendances
Pour installer les bibliothèques nécessaires, vous pouvez utiliser `pip` :
```bash
pip install pandas
```

### Fichiers d'entrée
Assurez-vous d'avoir les fichiers suivants dans le même répertoire que les scripts Python :
- `liste_20_actions.csv` : Utilisé par le script `bruteforce.py`.
- `dataset2_Python+P7.csv` : Utilisé par le script `optimized.py`.

Ces fichiers doivent contenir les colonnes suivantes :
- **Actions** : Nom ou identifiant de l'action.
- **Coût** : Coût associé à une action (en euros).
- **Bénéfice** : Taux de bénéfice attendu (en pourcentage).

---

## Exécution des scripts

### 1. Approche brute-force
Ce script teste toutes les combinaisons possibles et calcule la combinaison offrant le meilleur profit dans la limite du budget.

Pour exécuter le fichier `bruteforce.py` :
```bash
python bruteforce.py
```

**Sortie attendue :**
- Liste des actions optimales.
- Somme totale investie.
- Profit total.
- Temps d’exécution.

---

### 2. Approche optimisée (Knapsack)
Ce script utilise l'algorithme du sac à dos pour réduire le temps d'exécution tout en fournissant des résultats optimaux.

Pour exécuter le fichier `optimized.py` :
```bash
python optimized.py
```

**Sortie attendue :**
- Liste des actions optimales.
- Somme totale investie.
- Profit total.
- Ratio coûts/bénéfices.
- Temps d'exécution.

---

## Résultats Comparatifs
Les deux scripts affichent leurs résultats en fonction de leur logique respective d'optimisation :

1. **Approche brute-force** : Simple mais coûteuse en temps, cette méthode devient rapidement inefficace pour des listes d'actions importantes (en raison de la hausse exponentielle des combinaisons).
2. **Approche optimisée** : Plus performante pour gérer de larges ensembles de données grâce à des optimisations en programmation dynamique.

| Critère                  | Brute-force             | Algorithme optimisé          |
|-------------------------|-------------------------|------------------------------|
| Complexité              | Très élevée (exponentielle) | Moyenne (pseudo-polynomiale) |
| Efficacité              | Faible sur gros ensembles | Excellente                   |
| Temps d'exécution       | Long                    | Court                        |

---

## Améliorations possibles
- Ajouter une interface utilisateur graphique (GUI) ou des options en ligne de commande pour une meilleure interactivité.
- Implémenter une méthode hybride pour combiner rapidité et précision.
- Intégrer davantage de sources de données pour rendre le système plus performant et dynamique.
- Tester avec des jeux de données plus volumineux et mesurer les performances.

---

## Structure du projet
```
├── bruteforce.py               # Script utilisant la méthode brute-force
├── optimized.py                # Script utilisant l'algorithme du sac à dos
├── liste_20_actions.csv        # Dataset pour le script brute-force
├── dataset2_Python+P7.csv      # Dataset pour le script optimisé
├── README.md                   # Documentation du projet
```

---

## Auteur
Créé par **A'nsi**.
