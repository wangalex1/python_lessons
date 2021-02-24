class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for x in range(len(other.my_list[i])):
                self.my_list[i][x] = self.my_list[i][x] + other.my_list[i][x]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_new = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m + m_new)
