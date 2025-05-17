def main():
    # Create a 5x3 matrix
    m = [[0 for i in range(3)] for j in range(5)]
    x = 1
    
    # Populate the matrix
    for row in range(5):
        for col in range(3):
            m[row][col] = x
            x += 1
    
    # Print the matrix in a more readable format
    for row in m:
        print(row)

main()