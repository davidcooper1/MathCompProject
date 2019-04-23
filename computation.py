class Vector :
    """
        This class is meant to represent a mathematical vector.
        It will overload standard operators in order to make use of these vectors more natural.
    """

    VERTICAL = 0
    HORIZONTAL = 1

    def __init__(self, val=[0], orientation=VERTICAL) :
        self.val = val
        self.orientation = orientation

    def __str__(self) :
        return str(self.val)

    def __len__(self) :
        return len(self.val)

    def __getitem__(self, index) :
        return self.val[index]

    def __setitem__(self, index, value) :
        self.val[index] = value
        return self.val[index]

    def __neg__(self) :
        return Vector([-self[i] for i in range(len(self))], self.orientation)

    def __pos__(self) :
        return Vector(self.val, self.orientation)

    def __add__(self, other) :
        if type(other) is Vector :
            if len(self) == len(other) :
                return Vector([self[i] + other[i] for i in range(len(self))], self.orientation)
            else :
                raise TypeError("Vectors are of incompatible dimensions: {} and {}".format(len(self), len(other)))
        else :
            return NotImplemented

    def __sub__(self, other) :
        return self.__add__(-other)

    def dot(self, other) :
        if type(other) is Vector:
            if len(self) == len(other) :
                mult = [self[i] * other[i] for i in range(len(self))]
                result = 0
                for i in range(len(mult)) :
                    result += mult[i]
                return result
            else :
                raise TypeError("Vectors are of incompatible dimensions: {} and {}".format(len(self), len(other)))
        else :
            raise TypeError("Expected Vector but found type {}".format(type(other)))

    def __mul__(self, other) :
        if type(other) is int or type(other) is float or type(other) is complex :
            return Vector([self[i] * other for i in range(len(self))], self.orientation)
        else :
            return NotImplemented

    def __rmul__(self, other) :
        if type(other) is int or type(other) is float or type(other) is complex :
            return Vector([self[i] * other for i in range(len(self))], self.orientation)
        else :
            return NotImplemented

    def transpose(self) :
        return Vector(self.val, 1 ^ self.orientation)

class Matrix :

    @staticmethod
    def zeros(rows, cols) :
        return Matrix([[0 for col in range(cols)] for row in range(rows)])

    @staticmethod
    def ones(rows, cols) :
        return Matrix([[1 for col in range(cols) for row in range(rows)]])

    def __init__(self, val=[[0]]) :
        self.val = val

    def __str__(self) :
        return str(self.val)

    def __getitem__(self, index) :
        return self.val[index]

    def cols(self) :
        if len(self.val) > 0 :
            return len(self.val[0])
        return 0

    def rows(self) :
        return len(self.val)

    def col(self, index) :
        if index >= self.cols() :
            raise KeyError("Index is out of bounds.")
        result = [0] * self.rows();
        for i in range(self.rows()) :
            result[i] = self.val[i][index]
        return Vector(result, Vector.HORIZONTAL)

    def row(self, index) :
        if index >= self.rows() :
            raise KeyError("Index is out of bounds.")
        return Vector(list(self.val[index]), Vector.VERTICAL)

    def __mul__(self, other) :
        if type(other) is Matrix :
            if self.cols() != other.rows() :
                raise TypeError("Matrices are of incompatible dimensions: ({}, {}), ({}, {})".format(self.rows(), self.cols(), other.rows(), other.cols()))
            return Matrix([
                [
                    self.row(row).dot(other.col(col))
                    for col in range(other.cols())
                ] for row in range(self.rows())
            ])
        elif type(other) is Vector :
            if other.orientation == Vector.VERTICAL :
                if self.cols() != len(other) :
                    raise TypeError("Matrix and Vector have incompatible dimensions: ({}, {}), {}".format(self.rows(), self.cols(), len(other)))
                return Vector([
                    self.row(row).dot(other) for row in range(self.rows())
                ], Vector.VERTICAL);
            else :
                raise TypeError("Expected Vector in vertical orientation.")
        elif type(other) is int or type(other) is float or type(other) is complex :
            return Matrix([
                [
                    self.val[row][col] * other for col in range(self.cols())
                ] for row in range(self.rows())
            ])
        else :
            return NotImplemented

    def __rmul__(self, other) :
        return self.__mul__(other)

    def transpose(self) :
        return Matrix([
            self.col(i).val for i in range(self.cols())
        ])
