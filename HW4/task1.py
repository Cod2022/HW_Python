# Напишите функцию для транспонирования матрицы

matrix = [[1, 23], [42, 5], [7, 8]]

def matrix_transposition(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(matrix_transposition(matrix))
        

