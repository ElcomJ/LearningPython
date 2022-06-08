# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

a1 = input('Digite algo: ')

print(a1.isnumeric())                       # Verifica se o valor digitado é númerico e retorna True or False
print(a1.isalpha())                         # Verifica se o valor digitado é alfabético e retorna True or False
print(a1.isspace())                         # Verifica contém espaços na mensagem recebida e retorna True or False
print(a1.isalnum())                         # Verifica se o valor digitado é alfa-numérico e retorna True or False
print(a1.isupper())                         # Verifica se o valor digitado é UPPERCASE e retorna True or False
print(a1.istitle())                         # Verifica se o valor esla Capitalizado e retonra True or False

print('{}'.format(type(int(a1))))           # Transforma o valor da variável de str para int 
print('{}'.format(type(a1)))
print('{}'.format(type(float(a1))))         # Transforma o valor da variável de str para float
print('{}'.format(type(a1)))
