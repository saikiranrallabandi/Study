package main

import "fmt"

// MatrixMultiply multiplies two matrices A and B
func MatrixMultiply(A, B [][]int) [][]int {
	// Get dimensions
	rowsA := len(A)
	colsA := len(A[0])
	colsB := len(B[0])

	// Create result matrix filled with zeros
	result := make([][]int, rowsA)
	for i := range result {
		result[i] = make([]int, colsB)
	}

	// Triple nested loop for multiplication
	for i := 0; i < rowsA; i++ {
		for j := 0; j < colsB; j++ {
			for k := 0; k < colsA; k++ {
				result[i][j] += A[i][k] * B[k][j]
			}
		}
	}

	return result
}

// PrintMatrix prints a matrix in readable format
func PrintMatrix(matrix [][]int, name string) {
	fmt.Printf("\n%s:\n", name)
	for _, row := range matrix {
		fmt.Println(row)
	}
}

func main() {
	// Define matrices A and B
	A := [][]int{{1, 2}, {2, 3}}
	B := [][]int{{4, 5}, {6, 7}}

	// Print input matrices
	PrintMatrix(A, "Matrix A")
	PrintMatrix(B, "Matrix B")

	// Multiply matrices
	result := MatrixMultiply(A, B)

	// Print result
	PrintMatrix(result, "A × B (Result)")

	// Print calculation details
	fmt.Println("\n--- Calculation Details ---")
	fmt.Println("Position [0,0]: 1*4 + 2*6 = 16")
	fmt.Println("Position [0,1]: 1*5 + 2*7 = 19")
	fmt.Println("Position [1,0]: 2*4 + 3*6 = 26")
	fmt.Println("Position [1,1]: 2*5 + 3*7 = 31")
}
