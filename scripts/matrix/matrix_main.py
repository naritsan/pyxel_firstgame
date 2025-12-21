import sys
from scripts.libraries.pyxel_matrix import Matrix

def main():
    matrix1:Matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    matrix2:Matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    matrix3:Matrix = Matrix([[1,2,3],[4,5,6],[11,8,10]])
    matrix4:Matrix = Matrix([[1],[2],[3]])

    rndm1 = Matrix.create_random_3X3_matrix(123)
    rndm2 = Matrix.create_random_3X3_matrix(123)
    print(rndm1 == rndm2)

    print("muilply3x3")
    matrix1.print_all() 
    print(" * ")
    matrix2.print_all()
    print(" = ")
    (Matrix.multiply_3X3_matrices(matrix1,matrix2)).print_all()
    print("multiply3X1")
    matrix3.print_all() 
    print(" * ")
    matrix4.print_all()
    print(" = ")
    (Matrix.multiplyMatrixNxM(matrix3,matrix4)).print_all()


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit