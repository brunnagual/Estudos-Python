# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

#Pega inputs do usuário
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

#Exibo os resultados do código
print(f'Olá, {nome}! ')
# Essa operação :.2f significa que quero colocar um float com até duas casas decimais
print(f'Seu nome tem {len(nome):.2f} letras.')
print(f'Daqui 5 anos você terá {int(idade) + 5} anos.')