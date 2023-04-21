from sinac.core import *

def develop(expr):
    # do the development a*(b+c) = a*b + a*c
    
    # check if expression is in the form a*(b+c)
    if isinstance(expr, BinaryOperation) and isinstance(expr.right, BinaryOperation):

        if expr.op is Operator.MULT and expr.right.op is Operator.PLUS:
            # identify a, b and c in the formula 
            a = expr.left
            b = expr.right.left
            c = expr.right.right
        else:
            raise Exception('development not possible')
    
    # check if expression is in the form (b+c)*a
    elif isinstance(expr, BinaryOperation) and\
            isinstance(expr.left, BinaryOperation):
        
        if expr.op is Operator.MULT and expr.left.op is Operator.PLUS:
            # identify a, b and c in the formula
            a = expr.right
            b = expr.left.left
            c = expr.left.right
        else:
            raise Exception('development not possible')
    else:
        raise Exception('development not possible')


    # then apply the transformation law
    # (a + b) * c = a*c + b*c
    new_left = BinaryOperation(a, Operator.MULT, c)
    new_op = Operator.PLUS
    new_right = BinaryOperation(b, Operator.MULT, c)
    return BinaryOperation(new_left, new_op, new_right)

def factor(expr):
    # factor out: a*b + a*c = a*(b+c)
  
    # check that the expression is of the form x*y + a*b
    if isinstance(expr, BinaryOperation) and\
            isinstance(expr.left, BinaryOperation) and\
            isinstance(expr.right, BinaryOperation):
        if expr.op is Operator.PLUS and\
                expr.left.op is Operator.MULT and\
                expr.right.op is Operator.MULT:

            # there must be a more elegant way of doing this...
            # identify what is a, b and c in the formula
            if expr.left.left == expr.right.left:
                # a*b + a*c
                a = expr.left.left
                b = expr.left.right
                c = expr.right.right
            elif expr.left.left == expr.right.right:
                # a*b + c*a
                a = expr.left.left
                b = expr.left.right
                c = expr.right.left
            elif expr.left.right == expr.right.left:
                # b*a + a*c
                a = expr.left.right
                b = expr.left.left
                c = expr.right.right
            elif expr.left.right == expr.right.right:
                # b*a + c*a
                a = expr.left.right
                b = expr.left.left
                c = expr.right.left
            else:
                raise Exception('factorization not possible')

        else:
            raise Exception('factorization not possible')
    else:
        raise Exception('factorization not possible')
    
    # substitute to a*(b+c)
    new_left = a
    new_op = Operator.MULT
    new_right = BinaryOperation(b, Operator.PLUS, c)
    return BinaryOperation(new_left, new_op, new_right)
