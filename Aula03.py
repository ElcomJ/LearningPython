# Desafio01 - Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado. - FEITO

nome = input('Qual é o seu nome?')

print('Olá ' + nome + ' ! Prazer em te conhecer!')


# Desafio02 - Crie um script python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada


dia = input('Dia: ')
mes = input('Mes: ')
ano = input('Ano: ')

print('Você nasceu no dia ',dia,' de ',mes,' de ',ano,'. Correto?')


# Desafio03 - Crie um script python que leia dois números e tente mostrar a soma deles.


num1 = input('Primeiro número: ')
num2 = input('Segundo número: ')

soma = int(num1) + int(num2) #Precisar passa o tipo do número para poder ser reconhecido como uma váriavel númerica

print('A soma de ',num1,' e de ',num2,' é de: ',soma)