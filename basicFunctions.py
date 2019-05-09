def _abs(n) :
    """Computes the absolute value of a number.

    Given any number real or complex, this function returns its
    absolute value.

    Args:
        n (int/float/complex): The number to find the absolute value of.

    Returns:
        float: The absolute value of n.

    """
    return ((n.real ** 2) + (n.imag ** 2)) ** (1/2)

def _sum(iter) :
    """Computes the sum of all elements in an iterable.

    This function will loop through all elements of the iterable,
    iter, and compute their sum. It assumes that all of the elements
    of iter are of a numerical type.

    Args:
        iter (iterable): The iterable containing all the numbers to sum.

    Returns:
        (int/float/complex): The sum of the elements in the iterable.

    """

    result = 0
    for x in iter :
        result += x
    return result

def _conjugate(n) :
    """Computes the complex conjugate of a number.

    This function will compute the complex conjugate of a number by
    constructing a new complex number from the real part of the numbers
    with the negatiion of the imaginary part of the number.

    Args:
        n (int/float/complex): The number to find the complex conjugate of.

    Returns:
        (int/float): If the number is not a complex number, do nothing.
        (complex): If the number is complex, return its conjugate.

    """

    if (type(n) is int or type(n) is float) :
        return n;
    return complex(n.real, -n.imag)

def scalarVecMulti(n, v) :
    """Computes the result of scalar vector multiplication.

    This function takes a vector and multiplies all of its elements
    by a number to create a new vector.

    Args:
        n (int/float/complex): The number to multiply by all vector elements.
        v (list): The list of numbers representing the vector to be multiplied.

    Returns:
        (list): The result of multiplying every element of v by n.

    """
    return [n * v[i] for i in range(len(v))]

def conjTransMat(M) :
    """ Computes the complex conjugate of a matrix.

    This function flips the indices of the matrix M and computes the
    complex conjugate of all the entries in the matrix.

    Args:
        M (list): This is a list of lists representing a matrix to find the conjugate transpose of.

    Returns:
        (list): The list of lists representing a matrix that is the conjugate transpose of M.

    """

    return [
        [_conjugate(M[j][i]) for j in range(len(M)) ] for i in range(len(M[0]))
    ]

def conjTransVec(v) :
    """Computes the conjugate transpose of a vector.

    This function takes the conjugate of every number in the
    list representing a vector.

    Args:
        v (list): This is the vector from which the complex transpose is found.

    Returns:
        (list): The complex transpose of the list v.

    """

    return [_conjugate(v[i]) for i in range(len(v))]

def pNorm(v, p=2) :
    """Computes the pNorm of a vector.

    This function sums up all the elements of v raised to the p power
    and then finds the pth root of the result of the sum.

    Args:
        v (list): A list representing a vector.
        p (int): The power to be used for the norm operation. Defaults to 2.

    Returns:
        (int/float): The p-norm of v. Always greater than zero.

    """

    return _sum([_abs(x) ** p for x in v]) ** (1 / p)

def dotProduct(x, y) :
    """Computes the dot product of two vectors.

    This function sums the list formed by multiplying every element of one
    vector with its corresponding element in another vector. It is assumed
    that the lists are of equal length.

    Args:
        x (list): The list representing the first vector.
        y (list): The list representing the second vector.

    Returns:
        (int/float/complex): The number representing the dot product of x and y.

    """
    return sum([x[i] * y[i] for i in range(len(x))])

def vectorAdd(x, y) :
    """Computes the result of the addition of two vectors.

    This function returns a list in which every element from list x
    has been added to its corresponding element in list y. It is assumed
    the length of x and y match.

    Args:
        x (list): The list representing the first vector.
        y (list): The list representing the second vector.

    Returns:
        (list): The result of vector addition between x and y.

    """

    return [x[i] + y[i] for i in range(len(x))]

def vectorSub(x, y) :
    """Computes the result of subtraction between two vectors.

    This function returns a list in which every element of list y has been subtracted
    from its corresponding element in list x such that the result is equal to
    x - y. It is assumed the length of x and y match.

    Args:
        x (list): The list representing the first vector.
        y (list): The list representing the second vector.

    Returns:
        (list): The result of vector subtraction between x and y.

    """

    return vectorAdd(x, scalarVecMulti(-1, y))

def matRow(A, row) :
    """Returns a copy of a row of the matrix.

    This function takes a matrix of vertical vectors, A, and returns a copy
    of the specified row. It is assumed that the variable row is a valid
    row number (0 <= row <= len(A[0])).

    Args:
        A (list): This is a list of lists representing the matrix A.
        row (int): This is the number of the row to be returned.

    Returns:
        (list): The specified row of the matrix.

    """

    return [A[i][row] for i in range(len(A))]

def matrixMulti(A, B) :
    """Computes the result of matrix multiplication.

    This function takes two multidimensional lists representing
    matrices and multiplies them by computing the dot product of every
    row in A with every column in B. Forms the operation A * B.

    Args:
        A (list): Multidimensional list representing a matrix.
        B (list): Multidimensional list representing a matrix.

    Returns:
        (list): Multidimensional list representing the result.

    """

    return [
        [
            dotProduct(
                matRow(A, row),
                B[col]
            ) for row in range(len(A[0]))
        ] for col in range(len(B))
    ]

def matVecMulti(A, b) :
    """Computes the result of matrix vector multiplication.

    This fuction takes in a multidimensional list representing a matrix,
    A, and a list representing vector b. It then multiplies all the rows of
    A with b itself. b is assumed to be a column vector. A has the same number
    of columns as b has entries.

    Args:
        A (list): This is a multidimensional list representing a matrix.
        b (list): This list represents a vector.

    Returns:
        (list): This is a list representing a vector result.

    """

    return [
        dotProduct(matRow(A, row), b) for row in range(len(A[0]))
    ]

def vandermonde(x, n) :
    """Constructs a vandermonde matrix.

    This function takes in the list x, representing a vector, and
    transforms it into a vandermonde matrix of degree n.

    Args:
        x (list): List representing a vector.
        n (int): Number representing the degree.

    Result:
        (list): Multidimensional list representing the vandermonde matrix.

    """

    return [
        [x[i] ** j for i in range(len(x))] for j in range(n)
    ]

def modGramSchmidt(A) :
    """Computes the QR decomposition of a matrix

    This function uses the modified gram schmidt algorithm to calculate
    the QR decomposition of A. All matrices are represented as a set of
    column vectors.

    Args:
        A (list): Multidimensional list representing a matrix.

    Returns:
        (list, list): Returns the matrices Q and R represented by multidimensional lists.

    """

    Q = []
    R = [ [ 0 for i in range(len(A))] for j in range(len(A)) ]


    v = [ [ A[i][j] for j in range(len(A[0])) ] for i in range(len(A)) ]

    for j in range(len(v)) :
        R[j][j] = pNorm(v[j])
        Q.append(scalarVecMulti(1 / R[j][j], v[j]))

        for k in range(j+1, len(v)) :
            R[k][j] = dotProduct(conjTransVec(Q[j]), v[k])
            v[k] = vectorSub(v[k], scalarVecMulti(R[k][j], Q[j]))

    return Q, R

def backSub(A, b) :
    """Uses back substitution to solve a matrix system.

    This function takes in a multidimensional list, A, representing an upper
    triangular matrix and a vector representing the solutions for the system,
    and it computes the variables of the system.

    Args:
        A (list): Multidimensional list representing a matrix.
        b (list): List representing a vector.

    Returns:
        (list): The variables of the system.

    """

    result = [b[i] for i in range(len(b))]
    for i in range(len(A[0]) - 1, -1, -1) :
        result[i] = (b[i] - _sum([A[k][i] * result[k] for k in range(i + 1, len(A[0]))])) / A[i][i]
    return result

def interpolate(a, x) :
    """Calculates the interpolation of a polynomial.

    This function takes in a list of coefficients and calculates
    the solution to a polynomial of degree len(a) with coefficients
    a at x.

    Args:
        a (list): This is a list of numbers to be used a coefficients
        x (int/float/complex): This is a number to be plugged into the polynomial.

    """

    return _sum([a[i] * (x ** i) for i in range(len(a))])
