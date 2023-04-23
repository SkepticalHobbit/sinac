from sinac import core, menu

x = core.Symbol('x')
y = core.Symbol('y')
z = core.Symbol('z')

expr = x*(y+z) + y*(z+x) + z*(x+y) + z*(z+x)
menu.main(expr)
