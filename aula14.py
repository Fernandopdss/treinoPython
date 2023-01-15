while True:
    print("Isso é uma calculadora, insira os dados selecionados!")
    a = input('Insira um numero: ')
    b = input('Insira um Operador válido(+-*/): ')
    c = input('Insira um numero: ')
    d = None
    try:
        a = float(a)
        c = float(c)
        d = True
    except:
        d = None
        print('Foi inserido um número invalido!')
        continue

    if d is True:
        if b == '+':
            print(f'O resultado de {a} {b} {c} é: ', (a+c))

        elif b == '-':
            print(f'O resultado de {a} {b} {c} é: ', (a-c))

        elif b == '*':
            print(f'O resultado de {a} {b} {c} é: ', (a*c))

        elif b == '/':
            print(f'O resultado de {a} {b} {c} é: ', (a/c))
        else:
            print('Foi inserido um operador invalido') 
            continue

    sair = input('Deseja [s]air?').lower().startswith('s')
    if sair:
        break

