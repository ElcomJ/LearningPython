#Tipos primitivos e saidas de dados

#int   = número inteiro        | Ex: 1, 5, -4,884, 7, 0.
#float = número real           | Ex: 4.5, 0.075, -15.225, 3.14, 7.0.
#bool  = Valor verdadeiro      | Ex: True, False.
#str   = Cadeia de caracteres  | Ex: 'Olá', '7.5', ''.

n1=int(input('Digite um número: '))
n2=int(input('Digite outro numero: '))

soma=n1+n2

# print('A soma de ',n1,' e de ',n2,' é de: {}'.format(soma))
print('A soma entre {} e {} vale {}'.format(n1, n2, soma)) # A {} é utilizada para poder receber valores formatados com o .format
