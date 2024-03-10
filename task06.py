def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            total_cost += info['cost']
            total_calories += info['calories']
            chosen_items.append(item)

    return chosen_items, total_calories

def dynamic_programming(items, budget):
    # Створюємо матрицю для зберігання результатів підпроблем
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, (item, info) in enumerate(items.items(), 1):
        for j in range(1, budget + 1):
            if info['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - info['cost']] + info['calories'])
            else:
                dp[i][j] = dp[i - 1][j]

    chosen_items = []
    i = len(items)
    j = budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            chosen_items.append(list(items.keys())[i - 1])
            j -= items[chosen_items[-1]]['cost']
        i -= 1

    return chosen_items, dp[-1][-1]

# Задання страв
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Бюджет
budget = 100

# Виклик функцій
greedy_items, greedy_calories = greedy_algorithm(items, budget)
dp_items, dp_calories = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print("Обрані страви:", greedy_items)
print("Загальна кількість калорій:", greedy_calories)

print("\nАлгоритм динамічного програмування:")
print("Обрані страви:", dp_items)
print("Загальна кількість калорій:", dp_calories)