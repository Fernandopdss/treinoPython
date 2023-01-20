#esse programa acessa os itens de uma lista e os organiza em um formato de questions e respostas.
#é possivel adicionar mais questions seguindo o mesmo formato dos dicionarios dentro da lista e o programa funcionará normalmente mostrando as questions adicionadas.
questions = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5','45'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51','43'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1','7'],
        'Resposta': '5',
    },
]

count_question = 0
user_insert = 0
points = 0

print('Esse é um jogo de questions e respostas. Ao responder digite o numero da alternativa que você achar correta')

for i in questions:
    count_options = 0
    print(f'\nPergunta',questions[count_question]['Pergunta'])

    for i in questions[count_question]['Opções']:
        print(f'{count_options})',questions[count_question]['Opções'][count_options])
        count_options+=1

    user_insert = input(f'\nResposta: ')

    try:
        user_insert = int(user_insert)
        if questions[count_question]['Opções'][user_insert] == questions[count_question]['Resposta']:
            print(f'\nAcertou')
            points += 1
        else:
            print(f'\nerrou')
    except:
        print(f'\nerrou')

    count_question +=1

print(f'Você acertou {points} de {len(questions)} questions.')
input('feedback')

