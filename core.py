import enum

class Operator(enum.Enum):
    PLUS = '+'
    MULT = '*'
    POW  = '^'

    def __str__(self):
        return self.value

class Symbol(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def __add__(self, other):
        return BinaryOperation(self, Operator.PLUS, other)

    def __mul__(self, other):
        return BinaryOperation(self, Operator.MULT, other)

    def __str__(self):
        return self.symbol
    
    __repr__ = __str__

class BinaryOperation(object):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __add__(self, other):
        return BinaryOperation(self, Operator.PLUS, other)
    
    def __mul__(self, other):
        return BinaryOperation(self, Operator.MULT, other)

    def __str__(self):
        string = ''
        if not isinstance(self.left, Symbol):
            string += '('+str(self.left)+')'
        else:
            string += str(self.left)
        string += str(self.op)
        if not isinstance(self.right, Symbol):
            string += '('+str(self.right)+')'
        else:
            string += str(self.right)
        return string

    __repr__ = __str__

    def args(self):
        return [self.left, self.right]
