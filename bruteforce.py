import pandas as pd
import itertools


actions = [
    {"Actions": "Action-1", "Coût": 20, "Bénéfice (%)": 5},
    {"Actions": "Action-2", "Coût": 30, "Bénéfice (%)": 10},
    {"Actions": "Action-3", "Coût": 50, "Bénéfice (%)": 15},
    {"Actions": "Action-4", "Coût": 70, "Bénéfice (%)": 20},
    {"Actions": "Action-5", "Coût": 60, "Bénéfice (%)": 17},
    {"Actions": "Action-6", "Coût": 80, "Bénéfice (%)": 25},
    {"Actions": "Action-7", "Coût": 22, "Bénéfice (%)": 7},
    {"Actions": "Action-8", "Coût": 26, "Bénéfice (%)": 11},
    {"Actions": "Action-9", "Coût": 48, "Bénéfice (%)": 13},
    {"Actions": "Action-10", "Coût": 34, "Bénéfice (%)": 27},
    {"Actions": "Action-11", "Coût": 42, "Bénéfice (%)": 17},
    {"Actions": "Action-12", "Coût": 110, "Bénéfice (%)": 9},
    {"Actions": "Action-13", "Coût": 38, "Bénéfice (%)": 23},
    {"Actions": "Action-14", "Coût": 14, "Bénéfice (%)": 1},
    {"Actions": "Action-15", "Coût": 18, "Bénéfice (%)": 3},
    {"Actions": "Action-16", "Coût": 8, "Bénéfice (%)": 8},
    {"Actions": "Action-17", "Coût": 4, "Bénéfice (%)": 12},
    {"Actions": "Action-18", "Coût": 10, "Bénéfice (%)": 14},
    {"Actions": "Action-19", "Coût": 24, "Bénéfice (%)": 21},
    {"Actions": "Action-20", "Coût": 114, "Bénéfice (%)": 18},
]


def calculate_benefit_value(cost, benefit_percentage):
    benefit_value = benefit_percentage * cost / 100
    return benefit_value

# Iterate over each dictionary in the list and calculate the profit
for action in actions:
    cost = action["Coût"]
    benefit_percentage = action["Bénéfice (%)"]
    action["Valeur du bénéfice"] = calculate_benefit_value(cost, benefit_percentage)


max_budget = 500

#initialize the best combination
best_combination = []
best_profit = 0

# Test every combination
for n in range(1, len(actions) + 1):
    for combination in itertools.combinations(actions, n):
        total_cost = sum(action["Coût"] for action in combination)
        total_profit = sum(action["Valeur du bénéfice"] for action in combination)

        if total_cost < max_budget and total_profit > best_profit:
            best_combination = combination
            best_profit = total_profit

print("Meilleur combinaisons d'actions: ")
for action in best_combination:
    print(f"- {action['Actions']} (Coût : {action['Coût']}€, Bénéfice : {action['Valeur du bénéfice']}€)")

print(f"Profit Total: {best_profit}")