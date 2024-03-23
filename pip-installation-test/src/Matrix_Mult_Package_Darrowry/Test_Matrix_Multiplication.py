# Creating multiple unit tests to check the implementation of Matrix_Multiplication.py

import Matrix_Multiplication
import pytest
import tracemalloc
import cProfile
import logging

with cProfile.Profile() as pr:

# Begin memory allocation tracking
    tracemalloc.start()

    logging.info('Memory tracing has begun')

# Test of multiplication of two 2x2 matrices
    def test_Matrix_Mult_1():
        assert Matrix_Multiplication.Matrix_Multiplication([[1,2], [3,4]], [[5,6], [7,8]]) == [[19,22],[43,50]]

# Test of multiplication of two 3x3 matrices
    def test_Matrix_Mult_2():
        assert Matrix_Multiplication.Matrix_Multiplication([[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6],[7,8,9]]) == [[30, 36, 42], [66, 81, 96], [102, 126, 150]]

# Test of multiplication of non-square matrices, giving a 1x1 matrix as result (A = 1x2 matrix, b = 2x1 matrix)
    def test_Matrix_Mult_3():
        assert Matrix_Multiplication.Matrix_Multiplication([[1,2]], [[1],[2]]) == [[5]]

# Test of improper matrix multiplication (A = 3x3 matrix, B = 2x3 matrix)

    def test_Matrix_Mult_4():
        assert Matrix_Multiplication.Matrix_Multiplication([[1,2,3],[4,5,6],[7,8,9]], [[4,5,6],[7,8,9]]) == 'Matrices have incompatible dimensions'


# Test to make sure error is caught for incorrect input in a matrix
    def test_Matrix_Mult_5():
        with pytest.raises(TypeError):
            Matrix_Multiplication.Matrix_Multiplication([["1",2]], [[1],[2]]) == [[5]]

    logging.warning('Test 5 (line 35) to check for a type error')

# Check the current and peak size of the traced memory blocks for the first six tests
    current_size1, current_peak1 = tracemalloc.get_traced_memory()

    tracemalloc.reset_peak()

# Test to for decimal inputs
    def test_Matrix_Mult_6():
        assert Matrix_Multiplication.Matrix_Multiplication([[0.5,2.0]], [[1.0],[2.00]]) == [[4.5]]

# Test to large number inputs in the matrix multiplication
    def test_Matrix_Mult_7():
        assert Matrix_Multiplication.Matrix_Multiplication([[10000000000,10000000000]], [[10000000000],[10000000000]]) == [[200000000000000000000]]

# Test of multiplication of larger matrices (both A and B 5x5)
    def test_Matrix_Mult_8():
        assert Matrix_Multiplication.Matrix_Multiplication([[1,1,1,1,1], 
                                                        [1,1,1,1,1],
                                                        [1,1,1,1,1],
                                                        [1,1,1,1,1],
                                                        [1,1,1,1,1]], [[1,1,1,1,1], 
                                                                        [1,1,1,1,1],
                                                                        [1,1,1,1,1],
                                                                        [1,1,1,1,1],
                                                                        [1,1,1,1,1]]) == [[5,5,5,5,5], 
                                                                                         [5,5,5,5,5],
                                                                                         [5,5,5,5,5],
                                                                                         [5,5,5,5,5],
                                                                                         [5,5,5,5,5]]

# Test to check for empty matrix input
    def test_Matrix_Mult_9():
        with pytest.raises(AssertionError):
            assert Matrix_Multiplication.Matrix_Multiplication([[]], [[1],[2]]) == [[]]

# Test to show that empty matrix input for A is caught by IF statement
    def test_Matrix_Mult_10():
        assert Matrix_Multiplication.Matrix_Multiplication([[]], [[1],[2]]) == 'Matrices have incompatible dimensions'

# Test to show that empty matrix input for B is caught by IF statement
    def test_Matrix_Mult_11():
        assert Matrix_Multiplication.Matrix_Multiplication([[1],[2]], [[]]) == 'Matrices have incompatible dimensions'

# Test to show that empty matrix input for B is caught by IF statement
    def test_Matrix_Mult_12():
        result = Matrix_Multiplication.Error_Function(2,0)
        return result


'''

# Check the current and peak size of the traced memory blocks for the first six tests
    current_size2, current_peak2 = tracemalloc.get_traced_memory()

    print(f"{current_size1=}, {current_peak1=}")
    print(f"{current_size2=}, {current_peak2=}")

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)

pr.print_stats()

#cProfile.run('test_Matrix_Mult_8()')

logging.error('Line 100 causes the Action Workflow to fail, so has been commented out')
'''