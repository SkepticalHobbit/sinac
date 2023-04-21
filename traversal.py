from sinac.core import *

def select_child(node):
    if isinstance(node, BinaryOperation):
        print('0) Back')
        print('1) ' + str(node.left))
        print('2) ' + str(node.right))
        choice = int(input())

        if choice == 0:
            return 'parent'
        if choice == 1:
            return node.left
        if choice == 2:
            return node.right
    else:
        print('0) Back')
        choice = int(input())

        if choice == 0:
            return 'parent'

def traversal(expr):
    traversal = [expr]

    while len(traversal) > 0:
        current_node = traversal[-1]
       
        print("\n=========================")
        print(current_node)
        
        selected_node = select_child(current_node)
        if selected_node == 'parent':
            traversal.pop()
        elif selected_node is not None:
            traversal.append(selected_node)
