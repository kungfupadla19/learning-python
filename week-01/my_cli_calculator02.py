n = int(input('Введите количество чисел в списке:'))
result = None

for i in range(1, n+1):
    chislo = int(input(f'Введите ваше {i} число:'))

    if result is None:
        result = chislo
    else:
        ops = input('Введите операцию:')
        if ops == '+':
            result += chislo
        elif ops == '-':
            result -= chislo
        elif ops == '*':
            result *= chislo
        elif ops == '/':
            result /= chislo
        else:
            print('Ошибка,неизвестная операция!')
            break

print(result)