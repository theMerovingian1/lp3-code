def fractional_knapsack(weights, profits, capacity):
    # Number of items
    n = len(weights)

    # Create a list of items with profit-to-weight ratio and index
    items = [(profits[i] / weights[i], weights[i], profits[i], i)
             for i in range(n)]

    # Sort items by their profit-to-weight ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)

    total_profit = 0.0  # Total profit in the knapsack
    fractions = [0.0] * n  # To store the fraction of each item taken

    for ratio, weight, profit, index in items:
        if capacity == 0:
            break
        # Take as much as possible of the current item
        take_weight = min(weight, capacity)
        fractions[index] = take_weight / weight
        total_profit += take_weight * ratio
        capacity -= take_weight

    return total_profit, fractions


if __name__ == "__main__":
    # User input for profits of the items
    profits = list(
        map(int, input("Enter the profits of the items separated by space: ").split()))

    # User input for weights of the items
    weights = list(
        map(int, input("Enter the weights of the items separated by space: ").split()))

    # User input for capacity of knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))

    total_profit, fractions = fractional_knapsack(weights, profits, capacity)

    print(f"Total Profit: {total_profit:.2f}")
    print("Fractions of each item taken:")
    for i, fraction in enumerate(fractions):
        print(f"Item {i+1}: {fraction:.2f}")
