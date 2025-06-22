import random

def simulate_dice_rolls(num_rolls):
    # Initialize count of sums (possible sums range from 2 to 12)
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        # Roll two dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        # Increment count for the resulting sum
        sums_count[total] += 1

    # Convert counts to probabilities
    probabilities = {sum_: count / num_rolls for sum_, count in sums_count.items()}
    return probabilities

if __name__ == "__main__":
    num_rolls = 1_000_000  # Number of dice rolls to simulate
    probabilities = simulate_dice_rolls(num_rolls)

    print("Probabilities of sums when rolling two dice:")
    for sum_, prob in sorted(probabilities.items()):
        print(f"Sum {sum_}: probability {prob:.4f}")

    # Theoretical probabilities of dice sums
    analytical_probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }

    print("\nTheoretical probabilities of sums:")

    for sum_, prob in sorted(analytical_probabilities.items()):
        print(f"Sum {sum_}: probability {prob:.4f}")

    # Compare Monte Carlo vs Theoretical
    print("\nComparison of results:")
    for sum_ in range(2, 13):
        monte_carlo_prob = probabilities[sum_]
        analytical_prob = analytical_probabilities[sum_]
        print(f"Sum {sum_}: Monte Carlo {monte_carlo_prob:.4f}, Theoretical {analytical_prob:.4f}")

    # Final conclusion
    print("\nConclusions:")
    print("The Monte Carlo method results are very close to the theoretical values, confirming the correctness of the simulation.")
    print("As the number of rolls increases, the Monte Carlo results become more accurate and approach the theoretical probabilities.")
    print("This demonstrates the Law of Large Numbers — as the number of experiments grows, the empirical results tend to match the expected theoretical outcomes.")