# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def transpose(matrix):
    result = []

    for column in range(len(matrix[0])):
        row = []

        for line in range(len(matrix)):
            row.append(matrix[line][column])

        result.append(row)

    return result
def add_matrices(matrix_a, matrix_b):
    result = []

    for row in range(len(matrix_a)):
        new_row = []

        for column in range(len(matrix_a[0])):
            new_row.append(matrix_a[row][column] + matrix_b[row][column])

        result.append(new_row)

    return result
def multiply_matrices(matrix_a, matrix_b):
    result = []

    for row in range(len(matrix_a)):
        new_row = []

        for column in range(len(matrix_b[0])):
            total = 0

            for k in range(len(matrix_b)):
                total += matrix_a[row][k] * matrix_b[k][column]

            new_row.append(total)

        result.append(new_row)

    return result
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(value) for value in row))

def read_matrix(rows, columns):
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        while len(row) != columns:
            print("Please enter exactly", columns, "numbers.")
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        matrix.append(row)

    return matrix

rows_a = int(input("Enter number of rows for matrix A: "))
columns_a = int(input("Enter number of columns for matrix A: "))
print("Enter matrix A:")
matrix_a = read_matrix(rows_a, columns_a)
print("Original Matrix A:")
print_matrix(matrix_a)

rows_b = int(input("Enter number of rows for matrix B: "))
columns_b = int(input("Enter number of columns for matrix B: "))
print("Enter matrix B:")
matrix_b = read_matrix(rows_b, columns_b)
print("Original Matrix B:")
print_matrix(matrix_b)
print("Transpose of Matrix A:")
transposed_a = transpose(matrix_a)     
print_matrix(transposed_a)  
print("Transpose of Matrix B:")
transposed_b = transpose(matrix_b)
print_matrix(transposed_b)
if rows_a == rows_b and columns_a == columns_b:
    print("Sum of Matrix A and Matrix B:")
    sum_matrix = add_matrices(matrix_a, matrix_b)
    print_matrix(sum_matrix)
else:
    print("Matrices A and B must have the same dimensions for addition.")

if columns_a == rows_b:
    print("Product of Matrix A and Matrix B:")
    product_matrix = multiply_matrices(matrix_a, matrix_b)
    print_matrix(product_matrix)
else:
    print("Incompatible matrix dimensions for multiplication.")
    