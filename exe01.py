# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

#Pega inputs do usuário
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
#Crio variáveis para facilitar o entendimento.
num_letras = len(nome)
idade_mais_velho = int(idade) + 5
#Exibo os resultados do código
print('Oi ' + nome)
print('Seu nome tem {} letras.'.format(num_letras))
print('Daqui 5 anos você terá {} anos.'.format(idade_mais_velho))