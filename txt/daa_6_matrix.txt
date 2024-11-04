import threading
import time

# Standard matrix multiplication (single-threaded)


def matrix_multiply_single(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # Initialize result matrix with zeroes
    result = [[0] * cols_B for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Multithreaded matrix multiplication (one thread per row)


def matrix_multiply_multithread(A, B):
    rows_A = len(A)
    cols_B = len(B[0])

    # Initialize result matrix with zeroes
    result = [[0] * cols_B for _ in range(rows_A)]

    # Function to compute one row of the result matrix
    def compute_row(row_index):
        for j in range(cols_B):
            result[row_index][j] = sum(A[row_index][k] * B[k][j]
                                       for k in range(len(B)))

    # Create and start one thread per row
    threads = []
    for i in range(rows_A):
        thread = threading.Thread(target=compute_row, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return result

# Helper function to measure time


def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

# Helper function to get matrix input from user


def input_matrix(rows, cols, matrix_name):
    print(f"\nEnter the elements for matrix {matrix_name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element [{i+1}, {j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix


def main():
    # Input dimensions for matrices A and B
    rows_A = int(input("Enter number of rows for Matrix A: "))
    cols_A = int(input("Enter number of columns for Matrix A: "))
    rows_B = int(input("Enter number of rows for Matrix B: "))
    cols_B = int(input("Enter number of columns for Matrix B: "))

    # Check if matrices can be multiplied
    if cols_A != rows_B:
        print("Matrix multiplication not possible. Columns of A must equal rows of B.")
        return

    # Get matrices from user
    A = input_matrix(rows_A, cols_A, "A")
    B = input_matrix(rows_B, cols_B, "B")

    # Measure single-threaded matrix multiplication time
    result_single, time_single = measure_time(matrix_multiply_single, A, B)
    print(f"\nSingle-threaded execution time: {time_single:.5f} seconds")

    # Measure multithreaded matrix multiplication time
    result_multithread, time_multithread = measure_time(
        matrix_multiply_multithread, A, B)
    print(
        f"Multithreaded execution time (one thread/row): {time_multithread:.5f} seconds")

    # Display results
    print("\nResult of single-threaded multiplication:")
    for row in result_single:
        print(row)

    print("\nResult of multithreaded multiplication:")
    for row in result_multithread:
        print(row)

    # Check for zero time to avoid division by zero error
    if time_multithread > 0:
        print(
            f"\nPerformance improvement: {time_single / time_multithread:.2f}x")
    else:
        print("\nPerformance improvement cannot be calculated due to negligible execution time differences.")


if __name__ == "__main__":
    main()
