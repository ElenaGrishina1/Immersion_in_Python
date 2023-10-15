matrix = [[1, 2, 8], [6, 12, 10]]
print("Первоначальная матрица:\n", matrix)


def matrix_transposition(matrix):
    '''Функция для транспонирования матрицы'''
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)
print("Транспонированная матрица:")
matrix_transposition(matrix)