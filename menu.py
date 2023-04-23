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

def print_except(expr, except_expr):
    string = ''
    if expr != except_expr:
        if not isinstance(expr.left, Symbol):
            string += '('+print_except(expr.left, except_expr)+')'
        else:
            string += str(expr.left)
        string += str(expr.op)
        if not isinstance(expr.right, Symbol):
            string += '('+print_except(expr.right, except_expr)+')'
        else:
            string += str(expr.right)
    else:
        string = "#"

    return string


def main(expr):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    stdscr.keypad(True)

    # initialize colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, 226, -1)

    caughtExceptions = ""
    traversal = [expr]

    #try:
    while len(traversal) > 0:
        current_node = traversal[-1]
       
        stdscr.clear()

        expr_to_print = print_except(expr, current_node).split('#')
        stdscr.addstr(0, 0, expr_to_print[0])
        stdscr.addstr(str(current_node), curses.color_pair(1))
        stdscr.addstr(expr_to_print[1])
        
        stdscr.addstr(2, 0, 'D) Develop')
        stdscr.addstr(3, 0, 'F) Factor')
        stdscr.addstr(4, 0, 'Q) Exit')
        stdscr.refresh()

        choice = stdscr.getkey()

        if choice == 'KEY_UP':
            traversal.pop()
        if choice == 'KEY_DOWN':
            if not isinstance(current_node.left, Symbol):
                traversal.append(current_node.left)
        if choice == 'KEY_LEFT':
            if len(traversal) > 1:
                traversal.pop()
                current_node = traversal[-1]
                if not isinstance(current_node.left, Symbol):
                    traversal.append(current_node.left)
        if choice == 'KEY_RIGHT':
            if len(traversal) > 1:
                traversal.pop()
                current_node = traversal[-1]
                if not isinstance(current_node.right, Symbol):
                    traversal.append(current_node.right)
        
        if choice.lower() == 'd':
            new_expr = transform.develop(current_node)

            current_node.left = new_expr.left
            current_node.op = new_expr.op
            current_node.right = new_expr.right
        if choice.lower() == 'f':
            new_expr = transform.factor(current_node)

            current_node.left = new_expr.left
            current_node.op = new_expr.op
            current_node.right = new_expr.right
        if choice.lower() == 'q':
            break
    #except Exception as err:
    #    caughtExceptions = str(err)

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

    if "" != caughtExceptions:
        print(caughtExceptions)
