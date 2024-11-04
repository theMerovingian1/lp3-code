"""
    Rushikesh Borade BE Comp Roll no. 2
     Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and 
    bound strategy.
"""


def knapsack(v, w, n, W):
    # Initialize the table
    c = [[0 for _ in range(W + 1)] for y in range(n + 1)]

    # Build table c[][] in bottom-up manner
    for i in range(1, n + 1):
        for wt in range(1, W + 1):
            if w[i - 1] <= wt:
                c[i][wt] = max(v[i - 1] + c[i - 1]
                               [wt - w[i - 1]], c[i - 1][wt])
            else:
                c[i][wt] = c[i - 1][wt]

    # The maximum value that can be put in a knapsack of capacity W
    max_value = c[n][W]

    # Find which items are included in the optimal solution
    included_items = []
    wt = W
    for i in range(n, 0, -1):
        if c[i][wt] != c[i - 1][wt]:
            included_items.append(i)
            wt -= w[i - 1]
    return max_value, included_items


# Example usage
if __name__ == "__main__":
    # User input for values (profits) of the items
    v = list(map(int, input(
        "Enter the values (profits) of the items separated by space: ").split()))

    # User input for weights of the items
    w = list(
        map(int, input("Enter the weights of the items separated by space: ").split()))

    # User input for capacity of knapsack
    W = int(input("Enter the capacity of the knapsack: "))

    # Number of items
    n = len(v)

    max_value, included_items = knapsack(v, w, n, W)

    print(f"Maximum value in Knapsack = {max_value}")
    print(f"Items included in the knapsack: {included_items}")
