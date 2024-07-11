def transpose_matrix(matrix):  # Function to Compute the transpose of a 2D list (matrix)
    # Calculate Number of Rows and Columns in the Matrix
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    # Compute the Transpose
    transpose = [[matrix[row][col] for row in range(rows)] for col in range(cols)]

    return transpose


if __name__ == "__main__":
    try:
        # Get Number of Rows and Columns
        rows = int(input("Enter Number of Rows: "))
        cols = int(input("Enter Number of Columns: "))

        # Initialize Empty Matrix
        matrix = []

        # Get Matrix Elements Row-wise
        print("Enter Elements: ")
        for i in range(rows):
            row = []
            for j in range(cols):
                element = int(input())
                row.append(element)
            matrix.append(row)

        # Print Original Matrix
        print("Original Matrix:")
        for row in matrix:
            print(row)

        # Compute and Print Transposed Matrix
        transposed_matrix = transpose_matrix(matrix)
        print("\nTransposed Matrix:")
        for row in transposed_matrix:
            print(row)

    except ValueError:
        print(
            "Error: Please Enter Valid Integer Values for Matrix Dimensions and Elements."
        )
