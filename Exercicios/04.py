# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

a1 = input('Digite algo: ')
a2 = input('Digite algo: ')
a3 = input('Digite algo: ')
a4 = input('Digite algo: ')

print(a1.isnumeric())        # Verifica se o valor digitado é númerico e retorna True or False
print(a2.isalpha())          # Verifica se o valor digitado é alfabético e retorna True or False
print(a3.isalnum())          # Verifica se o valor digitado é alfa-numérico e retorna True or False
print(a4.isupper())          # Verifica se o valor digitado é UPPERCASE e retorna True or False

print('{}'.format(type(a1)))
print('{}'.format(type(a2)))
print('{}'.format(type(a3)))
print('{}'.format(type(a4)))