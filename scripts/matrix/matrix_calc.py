import sys

class Matrix:
    def __init__(self,index:list[list[float]]):
        self.index = index

    def printAll(self):
        for i, row in enumerate(self.index):
            for j, column in enumerate(row):
                print(f"index[{i}][{j}] : {column}")

def main():
    matrix1:Matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    matrix2:Matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    matrix3:Matrix = Matrix([[1,2,3],[4,5,6],[11,8,10]])
    # matrix1.printAll()

    for i in range(len(matrix1.index)):
        for j in range(len(matrix1.index[i])):
            print(matrix1.index[i][j])
            print(matrix2.index[i][j])
            if matrix1.index[i][j] != matrix2.index[i][j]:
                print('error')

    
    for i in range(len(matrix1.index)):
        for j in range(len(matrix1.index[i])):
            print(matrix1.index[i][j])
            print(matrix3.index[i][j])
            if matrix1.index[i][j] != matrix3.index[i][j]:
                print('error')



    

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit