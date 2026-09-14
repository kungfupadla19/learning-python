print('Простейший калькулятор')
op = (input('Введите операцию которую хотите провести с числами:'))
num1 = int(input('Введите ваше первое число:'))
num2 = int(input('Введите ваше второе число:'))
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print (num1 / num2)
elif op == '%':
    print(num1 % num2)
else:
    print('Операция не распознана')

