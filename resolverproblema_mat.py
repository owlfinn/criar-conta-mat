import random

e = 0
user_replay = int(input(f'Quantas vezes você quer jogar?: '))
def gerarproblema():
    op = ["+", "-", "*"]
    op = random.choice(op)

    p1 = random.randint(1, 10)
    p2 = random.randint(1, 10)

    ex = f'{p1} {op} {p2}'
    r = eval(ex)
    return ex, r

for i in range(user_replay):
    ex, r = gerarproblema()
    user_r = int(input(f'PROBLEMA {i+1}: {ex} '))
    
    while True:
        if user_r == r:
            break
        else:
            e += 1
            break

print(f'O seu total de acertos foi: {user_replay - e}')
