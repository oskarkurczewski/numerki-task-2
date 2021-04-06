import numpy as np

def jordan(matrix):
    rows = matrix.shape[0]
    result = np.zeros(rows, dtype = 'double')

    for i in range(rows):
        if matrix[i][i] == 0:
            counter = 1
            while (i + counter) < rows and matrix[i + counter][i] == 0:
                counter += 1

            if i + counter == rows:
                break

            for k in range(rows + 1):
                temp = matrix[i][k]
                matrix[i][k] = matrix[i + counter][k]
                matrix[i + counter][k] = temp

        for j in range(rows):
            if i != j:
                ratio = matrix[j][i] / matrix[i][i]

                for k in range(rows + 1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in range(rows):
        if abs(matrix[i][i]) <= 1.0 / (10**10) and abs(matrix[i][rows]) <= 1.0 / (10**10):
            result = "\nUkład nieoznaczony."
        elif abs(matrix[i][i]) <= 0.000005 and abs(matrix[i][rows]) >= 1.0 / (10**10):
            result = "\nUkład sprzeczny."
        else:
            result[i] = matrix[i][rows] / matrix[i][i]

    return result