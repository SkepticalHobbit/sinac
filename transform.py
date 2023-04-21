from sinac.core import *

def develop(mult_obj):
    # first check if mult object is indeed a multiplication
    if not isinstance(mult_obj, BinaryOperation) or mult_obj.op != Operator.MULT:
    	raise Exception('development not possible')

    # check if development is possible, that is, 
    # if mult object contains an add object, in the abstract form:
    # mult(add(a,b),c)

    if isinstance(mult_obj.left, BinaryOperation) and mult_obj.left.op == Operator.PLUS:
        add_obj = mult_obj.left
        c = mult_obj.right
    elif isinstance(mult_obj.right, BinaryOperation) and mult_obj.right.op == Operator.PLUS:
    	add_obj = mult_obj.right
    	c = mult_obj.left
    else:
    	raise Exception('development not possible')
    a = add_obj.left
    b = add_obj.right
    
    # then apply the transformation law
    # (a + b) * c = a*c + b*c
    return BinaryOperation(BinaryOperation(a, Operator.MULT, c), 
                           Operator.PLUS,
                           BinaryOperation(b, Operator.MULT, c))
