import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:
    print('*' * 10)
    print('Ronda: ', rounds)
    print('*' * 10)

    user_option = input('Elige una opción: piedra, papel o tijera: ')
    user_option = user_option.lower()
    rounds += 1

    if not user_option in options:
        print('Opción no válida')
        continue

    computer_option = random.choice(options)

    print('La opción del usuario es      : ', user_option)
    print('La opción de la computadora es: ', computer_option)


    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('Gana el usuario')
            user_wins += 1
            print('Puntaje del usuario: ', user_wins)
            print('Puntaje de la computadora: ', computer_wins)
        else:
            print('Papel gana a piedra')
            print('Gana la computadora')
            computer_wins += 1
            print('Puntaje del usuario: ', user_wins)
            print('Puntaje de la computadora: ', computer_wins)
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('Gana el usuario')
            user_wins += 1
            print('Puntaje del usuario: ', user_wins)
            print('Puntaje de la computadora: ', computer_wins)
        else:
            print('Tijera gana a papel')
            print('Gana la computadora')
            computer_wins += 1
            print('Puntaje del usuario: ', user_wins)
            print('Puntaje de la computadora: ', computer_wins)
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('Gana el usuario')
            user_wins += 1
            print('Puntaje del usuario: ', user_wins)
            print('Puntaje de la computadora: ', computer_wins)
        else:
            print('Piedra gana a tijera')
            print('Gana la computadora')
            computer_wins += 1
            print('Puntaje del usuario: ', user_wins)
            print('Puntaje de la computadora: ', computer_wins)
    if computer_wins == 3:
        print('La computadora es la vencedora')
        break
    if user_wins == 3:
        print('El usuario es el vencedor')
        break