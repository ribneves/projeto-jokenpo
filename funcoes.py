# Importar modulo choice da biblioteca random
from random import choice

# Função apenas para embelezar o código
def start()-> None:
    print('---------------------Vamos jogar jokenpô-------------------')
    print('-------Esolha entre as 3 opções disponíveis: (pedra) - (papel) - (tesoura)-------')

# Função para randomizar a escolha do computador
def pc_random_choice() ->str:  
    escolha_pc = choice(['pedra', 'papel', 'tesoura'])
    return escolha_pc


# Validação se a escolha do usuario está destro das possibilidades.
def validation_user_choice(user_choice: str) ->str:
    option_choices = ['pedra', 'papel', 'tesoura']
    while user_choice.isalpha() and user_choice.casefold():
        if user_choice in option_choices:
            return True
        else:
            return False
    else:
        return False



# Verificar quem ganhou usando como base as opções escolhidas
def result(user_choice: str, pc_choice: str) ->str:
    if user_choice == 'pedra' and pc_choice == 'tesoura':
        print(f'O usuário venceu, {user_choice} vence {pc_choice}')
    elif user_choice == 'tesoura' and pc_choice == 'papel':
        print(f'Usuário venceu. {user_choice} vence {pc_choice}')
    elif user_choice == 'papel' and pc_choice == 'pedra':
        print(f'Usuário venceu. {user_choice} vence {pc_choice}')
    elif user_choice == pc_choice:
        print(f'Ninguém ganhou, {user_choice} empata com {pc_choice}')
    else:
        print(f'O computador venceu, {pc_choice} vence {user_choice} ')


