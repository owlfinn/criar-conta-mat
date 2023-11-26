import random

def gerarproblema():
    op = ["+", "-", "*"]
    op = random.choice(op)

    p1 = random.randint(1, 10)
    p2 = random.randint(1, 10)

    ex = f'{p1} {op} {p2}'
    r = eval(ex) # faz o resultado da conta gerada aleatoriamente
    return ex, r
