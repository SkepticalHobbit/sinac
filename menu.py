import curses
from sinac.core import *
from sinac import transform

def transform_menu(window, node):
    window.addstr(2, 0, '1) Develop')
    window.addstr(3, 0, '2) Factor')
    choice = window.getkey()
    choice = int(choice)

    if choice == 1:
        return transform.develop(node)
    if choice == 2:
        return transform.factor(node)


def node_selector_child(window, node):
    if isinstance(node, BinaryOperation):
        window.addstr(2, 0, '0) Up')
        window.addstr(3, 0, '1) ' + str(node.left))
        window.addstr(4, 0, '2) ' + str(node.right))
        window.addstr(5, 0, '3) Select')
        window.refresh()
        choice = window.getkey()
        choice = int(choice)

        if choice == 0:
            return 'parent'
        if choice == 1:
            return node.left
        if choice == 2:
            return node.right
        if choice == 3:
            return node
    else:
        window.addstr(2, 0, '0) Up')
        window.addstr(3, 0, '1) Select')
        window.refresh()
        choice = window.getkey()
        choice = int(choice)

        if choice == 0:
            return 'parent'
        if choice == 1:
            return node

def main(expr):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    stdscr.keypad(True)

    caughtExceptions = ""
    traversal = [expr]

    try:
        while len(traversal) > 0:
            current_node = traversal[-1]
           
            stdscr.clear()
            stdscr.addstr(0, 0, str(expr))
            stdscr.addstr(1, 0, str(current_node))
            stdscr.addstr(2, 0, '1) Switch node')
            stdscr.addstr(3, 0, '2) Transform')
            stdscr.refresh()

            choice = stdscr.getkey()
            choice = int(choice)
            
            stdscr.clear()
            stdscr.addstr(0, 0, str(expr))
            stdscr.addstr(1, 0, str(current_node))
            
            if choice == 1:
                selected_node = node_selector_child(stdscr, current_node)
                if selected_node == 'parent':
                    traversal.pop()
                elif selected_node is not None:
                    traversal.append(selected_node)
            if choice == 2:
                new_expr = transform_menu(stdscr, current_node)

                current_node.left = new_expr.left
                current_node.op = new_expr.op
                current_node.right = new_expr.right
    except Exception as err:
        caughtExceptions = str(err)

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

    if "" != caughtExceptions:
        print(caughtExceptions)
