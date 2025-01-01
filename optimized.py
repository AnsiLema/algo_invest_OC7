import pandas as pd
import timeit

def script_knapsack():
    # Load data from a CSV file
    file_path = "liste_20_actions.csv"
    actions_df = pd.read_csv(file_path)

    # Exclude stocks with a cost of 0 or a profit rate of 0
    actions_df = actions_df[(actions_df["Coût"] > 0) & (actions_df["Bénéfice"] > 0)]

    # Calculate the “Earnings Value” for each stock
    actions_df["Valeur du bénéfice"] = actions_df["Coût"] * actions_df["Bénéfice"] / 100

    # Convert the DataFrame to a list of dictionaries for easier processing
    actions = actions_df.to_dict(orient="records")

    # Set the maximum budget
    max_budget = 500.00

    def knapsack(actions, max_budget):
        # Number of shares
        n = len(actions)

        # Initialize the dp array to store the maximum profits
        dp = [[0.0] * (int(max_budget * 100) + 1) for _ in range(n + 1)]  # Multiply by 100 to handle floats

        # Fill in the dp table
        for i in range(1, n + 1):
            cost = int(actions[i - 1]["Coût"] * 100)  # Convert to cents for indexing
            benefit = actions[i - 1]["Valeur du bénéfice"]
            for w in range(int(max_budget * 100) + 1):
                if cost > w:
                    dp[i][w] = dp[i - 1][w]  # This action cannot be included
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + benefit)

        # Rebuild the best combination of actions
        w = int(max_budget * 100)
        selected_actions = []
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_actions.append(actions[i - 1])
                w -= int(actions[i - 1]["Coût"] * 100)

        return selected_actions, dp[n][int(max_budget * 100)]

    # Solving the problem with the knapsack algorithm
    selected_actions, max_profit = knapsack(actions, max_budget)

    # Calculate the total cost of selected actions
    sum_of_costs = sum(action["Coût"] for action in selected_actions)

    # Show results
    print("Meilleure combinaison d'actions :")
    for action in selected_actions:
        print(f"- {action['Actions']} (Coût : {action['Coût']}€, Bénéfice : {action['Valeur du bénéfice']:.2f}€)")
    print(f"Somme Investie: {sum_of_costs:.2f}€")
    print(f"Profit Total : {max_profit:.2f}€")

execution_time = timeit.timeit(script_knapsack, number=1)
print(f"Execution time: {execution_time:.2f} secondes")
