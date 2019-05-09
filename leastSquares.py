from computation import vandermonde
from computation import modGramSchmidt
from computation import matVecMulti
from computation import conjTransMat
from computation import backSub
from computation import interpolate

def getCoefficients(x, y) :
    A = vandermonde(x, 3)
    Q,R = modGramSchmidt(A)
    b = matVecMulti(conjTransMat(Q), y)
    a = backSub(R, b)
    return a

a = getCoefficients([0,1,2,3,4], [0,1,4,9,16])
print(interpolate(a, 5))
