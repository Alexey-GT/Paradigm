# Процедурная парадигма — возможность переиспользования кода в программе
def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{i} * {j} = {i * j}')
        print('')


n = int(input('Input number n: '))
multiplication_table(n)

print('Another paradigm:')

# Структурная парадигма — быстрая проверка кода на работоспособность
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{i} * {j} = {i * j}')
    print('')
