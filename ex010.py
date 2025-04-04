#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere Dolar:6,18

reais = float(input('Digite o valor em Reais: '))
dolar = 6.18
conversao = reais / 6.18 

print(f'R%{reais} podem comprar {conversao:.2f} Dólares [Cotação 6,18]')