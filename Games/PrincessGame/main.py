from os import system


def tela_inicial(person):
    system('clear')
    print(f'''\n{players[person]["Nome"]}, seu objetivo é conquistar o amor de uma das princesas. 
Modifique seus atributos Aparencia (Ap), Carisma (Car) e Inteligência (Int) para conseguir.
''')

    for key, val in players[person].items():
        print(f'{key}: {val}')

    print(f'\nEnergia {energy}')
    print('''\n[1] Princesas        [5] Usar Regata
[2] Salão/Spa        [6] Votar no Bolsonaro/Lula
[3] Estudar          [7] Programar
[4] Sair c/ Amigos   [8] Tutorial
    ''')


def act8():
    system('clear') or None
    print('''Seu personagem possui 3 atributos e 
6 ações que podem incrementar ou diminuir em 1 os pontos de atributo do personagem.
Cada personagem possui 10 pontos de energia para realizar ações. Boa Sorte.
''')
    r = int(input('[1] Voltar: '))
    while r != 1:
        print('Opção Inválida')
        r = int(input('[1] Voltar: '))


def act7(person):
    system('clear')
    print('Você ficou um pouco mais chato.')
    print('\033[31mCarisma -1\033[m')
    players[person]['Car'] -= 1
    r = int(input('[1] Voltar: '))
    while r != 1:
        print('Opção Inválida')
        r = int(input('[1] Voltar: '))


def act6(person):
    system('clear')
    print('Você precisa estudar um pouco mais.')
    print('\033[31mInteligência -1\033[m')
    players[person]['Int'] -= 1
    r = int(input('[1] Voltar: '))
    while r != 1:
        print('Opção Inválida')
        r = int(input('[1] Voltar: '))


def act5(person):
    system('clear')
    print('Fora de Moda.')
    print('\033[31mAparencia -1\033[m')
    players[person]['Ap'] -= 1
    r = int(input('[1] Voltar: '))
    while r != 1:
        print('Opção Inválida')
        r = int(input('[1] Voltar: '))


def act4(person):
    system('clear')
    print('Ótima Noite')
    print('\033[32mCarisma +1\033[m')
    players[person]['Car'] += 1
    r = int(input('[1] Voltar: '))
    while r != 1:
        print('Opção Inválida')
        r = int(input('[1] Voltar: '))


def act3(person):
    system('clear')
    print('Fogo nos neurônios')
    print('\033[32mInteligência +1\033[m')
    players[person]['Int'] += 1
    r = int(input('[1] Voltar: '))
    while r != 1:
        print('Opção Inválida')
        r = int(input('[1] Voltar: '))


def act2(person):
    system('clear')
    print('Prazeroso e rejuvenescedor')
    print('\033[32mAparencia +1\033[m')
    players[person]['Ap'] += 1
    r = int(input('[1] Voltar: '))
    while r != 1:
        print('Opção Inválida')
        r = int(input('[1] Voltar: '))


def princesas(person, princes):
    print(f'\nVocê pede a princesa {npc[princes]["Nome"]} em namoro e ela responde...')
    print('Você é ')
    if players[person]["Ap"] == npc[princes]["Ap"] and players[person]["Car"] == npc[princes]["Car"] and \
            players[person]["Int"] == npc[princes]["Int"]:
        print("Perfeito")

    if players[person]["Ap"] < npc[princes]["Ap"]:
        print("muito feio")
    if players[person]["Car"] < npc[princes]["Car"]:
        print("muito chato")
    if players[person]["Int"] < npc[princes]["Int"]:
        print("muito burro")

    if players[person]["Ap"] > npc[princes]["Ap"]:
        print("muito vaidoso")
    if players[person]["Car"] > npc[princes]["Car"]:
        print("muito extrovertido")
    if players[person]["Int"] > npc[princes]["Int"]:
        print("muito nerd")

    r = int(input('[1] Voltar: '))
    while r != 1:
        print('Opção Inválida')
        r = int(input('[1] Voltar: '))


print('Bem vindo ao game')
players = [{'Nome': 'John', 'Ap': 2, 'Car': 2, 'Int': 6}, {'Nome': 'Mathew', 'Ap': 6, 'Car': 1, 'Int': 3},
           {'Nome': 'August', 'Ap': 4, 'Car': 5, 'Int': 1}]

npc = [{'Nome': 'Ieda', 'Ap': 3, 'Car': 10, 'Int': 7}, {'Nome': 'Celeste', 'Ap': 8, 'Car': 6, 'Int': 6},
       {'Nome': 'Hawise', 'Ap': 8, 'Car': 2, 'Int': 10}]

energy = 10
jogo = True
e = ' ' * 4
opc = -1
while jogo:
    if energy == 0:
        print('Você não tem mais energia. pressione enter...')
        input()
    while opc < 0 or opc > 2:
        print("Escolha seu Avatar: ")
        print(f'N°   Personagem   Aparencia   Carisma   Inteligência')
        for n, p in enumerate(players):
            print(n + 1, end=e)
            for v in p.values():
                print(f'{v:>8}', end=e)
            print()

        opc = int(input('N°: ')) - 1

    tela_inicial(opc)
    act = int(input("Digite sua ação: "))
    if act == 8:  # Tutorial
        act8()
    if act == 7 and energy > 0:  # igreja
        act7(opc)
        energy -= 1
    if act == 6 and energy > 0:  # Votar no Bolsonaro
        act6(opc)
        energy -= 1
    if act == 5 and energy > 0:  # Regata
        act5(opc)
        energy -= 1
    if act == 4 and energy > 0:  # Amigos
        act4(opc)
        energy -= 1
    if act == 3 and energy > 0:  # Estudar
        act3(opc)
        energy -= 1
    if act == 2 and energy > 0:  # Salão
        act2(opc)
        energy -= 1

    if act == 1:
        system('clear')
        print(f'N°   Princesa')
        for n, p in enumerate(npc):
            print(n + 1, end=e)
            print(p['Nome'])
        cpo = int(input('Escolha uma princesa: ')) - 1
        princesas(opc, cpo)
