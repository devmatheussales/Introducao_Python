'''import random
num = random.randint(0, 69)
print(num)'''

#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math 

num = float(input('Digite um número real para ver qual é a parte inteira:'))

print(f'A parte real de {num} é: {math.trunc(num)}')
