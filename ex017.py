#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o cumprimento da hipotenusa.


cateto1 = float(input('Digite o primeiro cateto: '))
cateto2 = float(input('Digite o segundo cateto: '))

hipotenusa = (cateto1**2 + cateto2**2)
hipotenusa = hipotenusa**(1/2)

print(f'A hipotenusa é : {hipotenusa: .2f} ')
