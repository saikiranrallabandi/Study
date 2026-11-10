import math


def matrix_multiply(A, B):
    """Multiply two matrices A and B without using numpy"""
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def determinant_2x2(matrix):
    """Calculate determinant of a 2x2 matrix"""
    if len(matrix) != 2 or len(matrix[0]) != 2:
        return "Error: Matrix must be 2x2"

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    det = (a * d) - (b * c)
    return det


def inverse_2x2(matrix):
    """Calculate inverse of a 2x2 matrix"""
    if len(matrix) != 2 or len(matrix[0]) != 2:
        return "Error: Matrix must be 2x2"

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    det = (a * d) - (b * c)

    if det == 0:
        return "Error: Matrix is singular (determinant = 0), cannot be inverted"

    inverse = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]

    return inverse


def cross_product_2d(u, v):
    """Calculate 2D cross product (returns scalar)"""
    if len(u) != 2 or len(v) != 2:
        return "Error: Vectors must be 2D"

    cross = (u[0] * v[1]) - (u[1] * v[0])
    return cross


def cross_product_3d(u, v):
    """Calculate 3D cross product (returns a vector)"""
    if len(u) != 3 or len(v) != 3:
        return "Error: Vectors must be 3D"

    cross = [
        (u[1] * v[2]) - (u[2] * v[1]),
        (u[2] * v[0]) - (u[0] * v[2]),
        (u[0] * v[1]) - (u[1] * v[0])
    ]
    return cross


def eigenvalues_2x2(matrix):
    """Calculate eigenvalues of a 2x2 matrix using quadratic formula"""
    if len(matrix) != 2 or len(matrix[0]) != 2:
        return "Error: Matrix must be 2x2"

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    # Characteristic equation: λ² - (a+d)λ + (ad-bc) = 0
    # This is of form: λ² - (trace)λ + (determinant) = 0
    trace = a + d  # Sum of diagonal elements
    det = (a * d) - (b * c)  # Determinant

    # Quadratic formula: λ = (trace ± √(trace² - 4*det)) / 2
    discriminant = (trace * trace) - (4 * det)

    if discriminant < 0:
        return "Error: Complex eigenvalues (discriminant < 0)"

    sqrt_discriminant = math.sqrt(discriminant)

    lambda1 = (trace + sqrt_discriminant) / 2
    lambda2 = (trace - sqrt_discriminant) / 2

    return [lambda1, lambda2]


def eigenvector_2x2(matrix, eigenvalue):
    """Calculate eigenvector for a given eigenvalue"""
    if len(matrix) != 2 or len(matrix[0]) != 2:
        return "Error: Matrix must be 2x2"

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    # Create (A - λI)
    A_minus_lambda_I = [
        [a - eigenvalue, b],
        [c, d - eigenvalue]
    ]

    # For eigenvector, we solve (A - λI)v = 0
    # Using the first row: (a-λ)v1 + b*v2 = 0
    # If b != 0: v = [b, -(a-λ)] or normalized [1, -(a-λ)/b]
    # If b == 0: use second row

    if abs(b) > 1e-10:  # b is not zero
        # v = [b, -(a-eigenvalue)]
        # Normalize to [1, -(a-eigenvalue)/b]
        v1 = 1
        v2 = -(a - eigenvalue) / b
        return [v1, v2]
    elif abs(c) > 1e-10:  # c is not zero
        # From second row: c*v1 + (d-λ)v2 = 0
        # v = [-(d-eigenvalue), c] or normalized [1, c/(d-eigenvalue)]
        v1 = 1
        v2 = c / (a - eigenvalue) if abs(a - eigenvalue) > 1e-10 else 0
        return [v1, v2]
    else:
        return [1, 0]  # Default eigenvector


def print_matrix(matrix, name):
    """Print matrix in a readable format"""
    print(f"\n{name}:")
    for row in matrix:
        print(row)


def print_vector(vector, name):
    """Print vector in a readable format"""
    print(f"{name}: {vector}")


if __name__ == "__main__":
    print("=" * 70)
    print("LINEAR ALGEBRA: MATRICES, VECTORS, AND EIGENVALUES")
    print("=" * 70)

    # ==================== MATRIX MULTIPLICATION ====================
    print("\n" + "=" * 70)
    print("1. MATRIX MULTIPLICATION")
    print("=" * 70)

    A = [[1, 2], [2, 3]]
    B = [[4, 5], [6, 7]]

    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")

    result = matrix_multiply(A, B)
    print_matrix(result, "A × B (Result)")

    # ==================== EIGENVALUES & EIGENVECTORS ====================
    print("\n" + "=" * 70)
    print("2. EIGENVALUES AND EIGENVECTORS (2x2)")
    print("=" * 70)

    # Example 1
    print("\n--- Example 1 ---")
    M1 = [[4, 1], [1, 3]]
    print_matrix(M1, "Matrix M")

    eigenvals_1 = eigenvalues_2x2(M1)
    print(f"\nEigenvalues: {eigenvals_1}")
    print(f"λ₁ = {eigenvals_1[0]:.4f}")
    print(f"λ₂ = {eigenvals_1[1]:.4f}")

    print(f"\nEigenvectors:")
    eigenvec_1_1 = eigenvector_2x2(M1, eigenvals_1[0])
    eigenvec_1_2 = eigenvector_2x2(M1, eigenvals_1[1])

    print_vector(eigenvec_1_1, f"v₁ (for λ₁ = {eigenvals_1[0]:.4f})")
    print_vector(eigenvec_1_2, f"v₂ (for λ₂ = {eigenvals_1[1]:.4f})")

    # Verify: A·v = λ·v
    print(f"\nVerification (A·v = λ·v):")
    Av1 = [M1[0][0] * eigenvec_1_1[0] + M1[0][1] * eigenvec_1_1[1],
           M1[1][0] * eigenvec_1_1[0] + M1[1][1] * eigenvec_1_1[1]]
    lambda_v1 = [eigenvals_1[0] * eigenvec_1_1[0],
                 eigenvals_1[0] * eigenvec_1_1[1]]
    print(f"A·v₁ = {[round(x, 4) for x in Av1]}")
    print(f"λ₁·v₁ = {[round(x, 4) for x in lambda_v1]}")

    # Example 2
    print("\n" + "-" * 70)
    print("\n--- Example 2 ---")
    M2 = [[2, 1], [1, 2]]
    print_matrix(M2, "Matrix M")

    eigenvals_2 = eigenvalues_2x2(M2)
    print(f"\nEigenvalues: {eigenvals_2}")
    print(f"λ₁ = {eigenvals_2[0]:.4f}")
    print(f"λ₂ = {eigenvals_2[1]:.4f}")

    print(f"\nEigenvectors:")
    eigenvec_2_1 = eigenvector_2x2(M2, eigenvals_2[0])
    eigenvec_2_2 = eigenvector_2x2(M2, eigenvals_2[1])

    print_vector(eigenvec_2_1, f"v₁ (for λ₁ = {eigenvals_2[0]:.4f})")
    print_vector(eigenvec_2_2, f"v₂ (for λ₂ = {eigenvals_2[1]:.4f})")

    # Verify: A·v = λ·v
    print(f"\nVerification (A·v = λ·v):")
    Av2 = [M2[0][0] * eigenvec_2_1[0] + M2[0][1] * eigenvec_2_1[1],
           M2[1][0] * eigenvec_2_1[0] + M2[1][1] * eigenvec_2_1[1]]
    lambda_v2 = [eigenvals_2[0] * eigenvec_2_1[0],
                 eigenvals_2[0] * eigenvec_2_1[1]]
    print(f"A·v₁ = {[round(x, 4) for x in Av2]}")
    print(f"λ₁·v₁ = {[round(x, 4) for x in lambda_v2]}")

    print("\n" + "=" * 70)
    print("\nKey Formula:")
    print("Characteristic Equation: det(A - λI) = 0")
    print("Eigenvalue Equation: A·v = λ·v")
    print("=" * 70)
