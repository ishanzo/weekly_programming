def matrix_addition(a, b):
    for row in range(len(a)):#row
        for col in range(len(a)):#col
            a[row][col] += b[row][col]#add
    return a 
