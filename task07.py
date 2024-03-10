import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Ініціалізуємо лічильник для кожної можливої суми
    sums_count = {i: 0 for i in range(2, 13)}

    # Виконуємо симуляцію кидків
    for _ in range(num_rolls):
        # Кидаємо два кубики
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        # Додаємо суму кидків до лічильника
        sums_count[roll1 + roll2] += 1

    # Обчислюємо ймовірність для кожної суми
    total_rolls = sum(sums_count.values())
    probabilities = {k: (v / total_rolls) * 100 for k, v in sums_count.items()}
    return probabilities

def plot_probabilities(probabilities):
    # Створюємо графік для відображення ймовірностей
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність, %')
    plt.title('Ймовірності суми після кидків двох кубиків')
    plt.xticks(range(2, 13))
    plt.show()

# Кількість кидків
num_rolls = 100000

# Викликаємо функцію симуляції
probabilities = simulate_dice_rolls(num_rolls)

# Виводимо ймовірності
for sum_value, probability in probabilities.items():
    print(f"Сума {sum_value}: Ймовірність {probability:.2f}%")

# Побудова графіка
plot_probabilities(probabilities)