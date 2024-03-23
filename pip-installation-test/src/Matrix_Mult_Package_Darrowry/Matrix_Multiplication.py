# Building out simple function, copying the following, with small adjustments:
# https://www.programiz.com/python-programming/examples/multiply-matrix

def Matrix_Multiplication(A, B):

    C = []

    # Check to make sure inner dimensions match
    if (range(len(A[0])) != range(len(B))) or A == [[]] or B == [[]]:
        return "Matrices have incompatible dimensions"
    else:
        # Change C to empty matrix of dimensions N * Y, borrowed from here: https://stackoverflow.com/questions/18449136/initialize-empty-matrix-in-python
        C = [ [ 0 for i in range(len(A)) ] for j in range(len(B[0])) ]

        # iterate through rows of A
        for i in range(len(A)):
            # iterate through columns of B
            for j in range(len(B[0])):
            # iterate through rows of B
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]
    
        return(C)

#Adding useless function to check Code Coverage is working properly
def Useless_Function():

    rogue_data = []
    
    return rogue_data

#Adding to test Error and Exception handling
#https://docs.python.org/3/tutorial/errors.html
def Error_Function(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)