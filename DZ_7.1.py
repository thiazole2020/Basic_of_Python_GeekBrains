class Matrix:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        my_str = []
        for i in (self.content):
            my_str.append(f'| {" ".join(map(str, i))} |\n')
        return ''.join(my_str)

    def __add__(self, matrix2):
        if len(self.content) != len(matrix2.content):
            raise ValueError("Количество строк матриц не совпадает!")
        elif len(self.content[0]) != len(matrix2.content[0]):
            raise ValueError('Количество столбцов матриц не совпадает!')
        else:
            k = 0
            new_matrix = []
            for i in self.content:
                new_matrix_str = []
                l = 0
                for j in i:
                    new_matrix_str.append(j + matrix2.content[k][l])
                    l += 1
                new_matrix.append(new_matrix_str)
                k += 1
        return Matrix(new_matrix)

matrix_1 = Matrix([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
matrix_2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
matrix_3 = matrix_2 + matrix_1
print(matrix_3)