import pandas as pd
import timeit

def script_knapsack():
    # Charger les données depuis un fichier CSV
    file_path = "liste_20_actions.csv"
    actions_df = pd.read_csv(file_path)

    # Calculer la “Valeur du bénéfice” pour chaque action
    actions_df["Valeur du bénéfice"] = actions_df["Coût"] * actions_df["Bénéfice"] / 100

    # Convertir le DataFrame en une liste de dictionnaires pour faciliter le traitement
    actions = actions_df.to_dict(orient="records")

    # Définir le budget maximum
    max_budget = 500

    def knapsack(actions, max_budget):
        # Nombre d'actions
        n = len(actions)

        # Initialiser le tableau dp pour stocker les bénéfices maximaux
        dp = [[0] * (max_budget + 1) for _ in range(n + 1)]

        # Remplir le tableau dp
        for i in range(1, n + 1):
            cost = actions[i - 1]["Coût"]
            benefit = actions[i - 1]["Valeur du bénéfice"]
            for w in range(max_budget + 1):
                if cost > w:
                    dp[i][w] = dp[i - 1][w]  # On ne peut pas inclure cette action
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + benefit)

        # Reconstruire la meilleure combinaison d'actions
        w = max_budget
        selected_actions = []
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_actions.append(actions[i - 1])
                w -= actions[i - 1]["Coût"]

        return selected_actions, dp[n][max_budget]

    # Résoudre le problème avec l'algorithme du sac à dos
    selected_actions, max_profit = knapsack(actions, max_budget)

    # Cost of investment
    sum_of_costs = 0

    # Afficher les résultats
    print("Meilleure combinaison d'actions :")
    for action in selected_actions:
        print(f"- {action['Actions']} (Coût : {action['Coût']}€, Bénéfice : {action['Valeur du bénéfice']:.2f}€)")
        sum_of_costs += action["Coût"]

    print(f"Somme Investie: {sum_of_costs}€")
    print(f"Profit Total : {max_profit:.2f}€")

execution_time = timeit.timeit(script_knapsack, number=1)
print(f"Execution time: {execution_time:.2f} secondes")
