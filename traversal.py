from sinac.core import *
from sinac import transform

def node_selector_child(node):
    if isinstance(node, BinaryOperation):
        print('0) Up')
        print('1) ' + str(node.left))
        print('2) ' + str(node.right))
        print('3) Select')
        choice = int(input())

        if choice == 0:
            return 'parent'
        if choice == 1:
            return node.left
        if choice == 2:
            return node.right
        if choice == 3:
            return node
    else:
        print('0) Up')
        print('1) Select')
        choice = int(input())

        if choice == 0:
            return 'parent'
        if choice == 1:
            return node

def node_selector(expr):
    traversal = [expr]

    while len(traversal) > 0:
        current_node = traversal[-1]
       
        print("\n=========================")
        print(current_node)

        selected_node = node_selector_child(current_node)
        if selected_node == 'parent':
            traversal.pop()
        elif selected_node == current_node:
            return selected_node
        elif selected_node is not None:
            traversal.append(selected_node)
    return None
    
