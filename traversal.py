from sinac.core import *
from sinac import transform

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

def select_node(expr):
    traversal = [expr]

    while len(traversal) > 0:
        current_node = traversal[-1]
       
        print("\n=========================")
        print(current_node)

        print("1) Change node")
        print("2) Select node") 
        choice = int(input())

        if choice == 1:
            selected_node = select_child(current_node)
            if selected_node == 'parent':
                traversal.pop()
            elif selected_node is not None:
                traversal.append(selected_node)
        if choice == 2:
            return current_node
