print("Isso é uma calculadora, insira os dados solicitados!")
while True:
    number1 = input('Insira um numero: ')
    operator = input('Insira um Operador válido(+-*/): ')
    number2 = input('Insira um numero: ')
    validadornmb = None
    try:
        number1 = float(number1)
        number2 = float(number2)
        validadornbm = True
    except:
        validadornbm = None
        print('Foi inserido um número invalido! Tente novamente')
        continue

    if operator not in '+-*/':
        print('Foi inserido um operador invalido! Tente novamente')
        continue

    elif operator == '+':
        print(f'O resultado de {number1} {operator} {number2} é: {number1 + number2:,.2f}')

    elif operator == '-':
        print(f'O resultado de {number1} {operator} {number2} é: {number1 - number2:,.2f}')

    elif operator == '*':
        print(f'O resultado de {number1} {operator} {number2} é: {number1 * number2:,.2f}')

    elif operator == '/':
        print(f'O resultado de {number1} {operator} {number2} é: {number1 / number2:,.2f}')

    sair = input('Deseja sair? Se sim digite [s]').lower().startswith('s')
    if sair:
        print('Calculadora encerrada!')
        break
    

