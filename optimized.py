import pandas as pd
import timeit

def script_knapsack():
    # Charger les données depuis un fichier CSV
    file_path = "dataset2_Python+P7.csv"
    actions_df = pd.read_csv(file_path)

    # Exclure les actions ayant un coût de 0 ou un taux de bénéfices de 0
    actions_df = actions_df[(actions_df["Coût"] > 0) & (actions_df["Bénéfice"] > 0)]

    # Calculer la “Valeur du bénéfice” pour chaque action
    actions_df["Valeur du bénéfice"] = actions_df["Coût"] * actions_df["Bénéfice"] / 100

    # Convertir le DataFrame en une liste de dictionnaires pour faciliter le traitement
    actions = actions_df.to_dict(orient="records")

    # Définir le budget maximum
    max_budget = 500.00

    def knapsack(actions, max_budget):
        # Nombre d'actions
        n = len(actions)

        # Initialiser le tableau dp pour stocker les bénéfices maximaux
        dp = [[0.0] * (int(max_budget * 100) + 1) for _ in range(n + 1)]  # Multiplie par 100 pour gérer les floats

        # Remplir le tableau dp
        for i in range(1, n + 1):
            cost = int(actions[i - 1]["Coût"] * 100)  # Convertir en centimes pour l'indexation
            benefit = actions[i - 1]["Valeur du bénéfice"]
            for w in range(int(max_budget * 100) + 1):
                if cost > w:
                    dp[i][w] = dp[i - 1][w]  # On ne peut pas inclure cette action
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + benefit)

        # Reconstruire la meilleure combinaison d'actions
        w = int(max_budget * 100)
        selected_actions = []
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_actions.append(actions[i - 1])
                w -= int(actions[i - 1]["Coût"] * 100)

        return selected_actions, dp[n][int(max_budget * 100)]

    # Résoudre le problème avec l'algorithme du sac à dos
    selected_actions, max_profit = knapsack(actions, max_budget)

    # Calculer le coût total des actions sélectionnées
    sum_of_costs = sum(action["Coût"] for action in selected_actions)

    # Afficher les résultats
    print("Meilleure combinaison d'actions :")
    for action in selected_actions:
        print(f"- {action['Actions']} (Coût : {action['Coût']}€, Bénéfice : {action['Valeur du bénéfice']:.2f}€)")
    print(f"Somme Investie: {sum_of_costs:.2f}€")
    print(f"Profit Total : {max_profit:.2f}€")

execution_time = timeit.timeit(script_knapsack, number=1)
print(f"Execution time: {execution_time:.2f} secondes")
