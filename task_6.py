def greedy_algorithm(items, budget):
    """Greedy algorithm to select items based on the highest calories per cost ratio."""
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, details in sorted_items:
        if details['cost'] <= budget:
            selected_items.append(item)
            total_calories += details['calories']
            budget -= details['cost']
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item, details = list(items.items())[i - 1]
        cost = details['cost']
        calories = details['calories']
        
        for w in range(budget + 1):
            if cost <= w: # If the item can be included
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories) 
            else:
                dp[i][w] = dp[i - 1][w]
    
    total_calories = dp[n][budget]
    selected_items = []
    w = budget
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, details = list(items.items())[i - 1]
            selected_items.append(item)
            w -= details['cost']
    
    return selected_items, total_calories

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    budget = 100
    
    greedy_result = greedy_algorithm(items, budget)
    print("Greedy Algorithm Result:")
    print("Selected Items:", greedy_result[0])
    print("Total Calories:", greedy_result[1])
    
    dp_result = dynamic_programming(items, budget)
    print("\nDynamic Programming Result:")
    print("Selected Items:", dp_result[0])
    print("Total Calories:", dp_result[1])