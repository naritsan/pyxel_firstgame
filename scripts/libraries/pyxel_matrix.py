import random

class Matrix:
    def __init__(self,index:list[list[float]]):
        self.index = index

    def print_all(self):
        for row in self.index:
            print("[",end="")
            for j, column in enumerate(row):
                print(f"{column}".center(5),end="")
                if j == len(row)-1:
                    print("]")
                else:
                    print(",",end="")


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented

        for i in range(len(self.index)):
            for j in range(len(self.index[i])):
                if self.index[i][j] != other.index[i][j]:
                    return False

        return True

    def __add__(self,other:Matrix) -> Matrix:
        tmp = Matrix([[0,0,0],[0,0,0],[0,0,0]])
        for i in range(len(self.index)):
            for j in range(len(self.index[i])):
                tmp.index[i][j] = self.index[i][j] + other.index[i][j]

        return tmp

    def __sub__(self,other:Matrix) -> Matrix:
        tmp = Matrix([[0,0,0],[0,0,0],[0,0,0]])
        for i in range(len(self.index)):
            for j in range(len(self.index[i])):
                tmp.index[i][j] = self.index[i][j] - other.index[i][j]

        return tmp

    def __mul__(self,scale:float) -> Matrix:
        tmp = Matrix([[0,0,0],[0,0,0],[0,0,0]])
        for i in range(len(self.index)):
            for j in range(len(self.index[i])):
                tmp.index[i][j] = self.index[i][j] * scale

        return tmp

    # 式の左右が逆の場合にも対応
    __rmul__ = __mul__


    @staticmethod
    def create_random_3X3_matrix(seed:int):
        rng:random.Random = random.Random(seed)
        tmp = Matrix([[0,0,0],[0,0,0],[0,0,0]])
        for i in range(3):
            for j in range(3):
                tmp.index[i][j] = rng.uniform(0,100)

        return tmp
        
    @staticmethod
    def multiply_3X3_matrices(m1:Matrix,m2:Matrix):
        tmp = Matrix([[0,0,0],[0,0,0],[0,0,0]])
        for i in range(len(m1.index)):
            for j in range(len(m1.index[i])):
                for k in range(3):
                    tmp.index[i][j] += (m1.index[i][k] * m2.index[k][j])

        return tmp

    @staticmethod
    def multiplyMatrixNxM(m1:Matrix,m2:Matrix):
        tmp = Matrix([[0],[0],[0]])
        for i in range(len(m1.index)):
            # print(f"i : {i}")
            for j in range(len(m1.index[i])):
                # print(f"j : {j}")
                tmp.index[i][0] += (m1.index[i][j] * m2.index[j][0])

        return tmp

