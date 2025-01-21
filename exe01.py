#Exercicio de Entrevista.

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