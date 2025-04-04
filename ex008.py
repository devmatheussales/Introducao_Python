#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('Digite o número de metros: '))

centimetros = metros * 100
milimetros = metros *1000

print(f'{metros}: Metros, equivalem a: {centimetros}cm ou {milimetros}mm')