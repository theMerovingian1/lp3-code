"""
    Rushikesh Borade BE Comp Roll no: 2
    Write a program non-recursive and recursive program to calculate Fibonacci numbers and 
    analyze their time and space complexity.
"""


def fibonacci_recursive_series(n):
    series = []
    for i in range(n + 1):
        series.append(fibonacci_recursive(i))
    return series


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_non_recursive_series(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]

    series = [0, 1]
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
        series.append(curr)

    return series


def fib_revursive_memo(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib_revursive_memo((n-2), memo) + fib_revursive_memo((n-1), memo)
    print(memo)
    return memo[n]


def main():
    while True:
        try:
            n = int(input("Enter the position of the Fibonacci sequence (n): "))
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        choice = input(
            "Choose method: (R)ecursive or (N)on-recursive? ").strip().lower()

        if choice == 'r':
            series = fibonacci_recursive_series(n)
            print(f"Fibonacci series up to position {n} (Recursive): {series}")
        elif choice == 'n':
            series = fibonacci_non_recursive_series(n)
            print(f"Fibonacci series position {n} (Non-recursive): {series}")
        elif choice == 'm':
            series = fib_revursive_memo(n)
            print(f"Fibonacci series position {n} (Non-recursive): {series}")
        else:
            print(
                "Invalid choice. Please enter 'R' for Recursive or 'N' for Non-recursive.")

        another = input(
            "Would you like to calculate another Fibonacci series? (y/n): ").strip().lower()
        if another != 'y':
            break


if __name__ == "__main__":
    main()
