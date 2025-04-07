#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.


import math

angulo = float(input('Digite o Angulo: '))


seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O angulo{angulo}, tem o SENO de {seno: .2f}, o COSSENO {cosseno: .2f} e TANGENTE de {tangente: .2f}')
