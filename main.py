# Importando funções.
from funcoes import *

# Variavél com função para randomizar escolha do computador.
computador = pc_random_choice()

# Inicio do jogo.
start()

# Pegar opção desejada pelo jogador.
jogador = input('Digite sua opção desejada: ')

# Tratamento para verificar se o jogador digitou corretamente e escolheu uma das opções válidas.
while validation_user_choice(jogador) == False:
    jogador = input('Opção invalida\nDigite novamente uma das opções disponíveis: ')
    
# Função para definir o ganhador.
resultado = result(jogador, computador)