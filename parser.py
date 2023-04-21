# parser basicao da massa só pra não ter que fazer tudo na mão
# por enquanto não leva em consideração parênteses e tal
def parse(str_exp):
    # tirar vírgulas
    str_exp = str_exp.replace(' ','')

    if len(str_exp.split('+')) > 1:
        left, right = str_exp.rsplit('+', 1)
        left = parse(left)
        right = parse(right)
        return BinaryOperation(left, Operator.PLUS, right)
    elif len(str_exp.split('*')) > 1:
        left, right = str_exp.rsplit('*', 1)
        left = parse(left)
        right = parse(right)
        return BinaryOperation(left, Operator.MULT, right)
    elif len(str_exp.split('^')) > 1:
        left, right = str_exp.rsplit('^', 1)
        left = parse(left)
        right = parse(right)
        return BinaryOperation(left, Operator.POW, right)
    else:
        return str_exp

