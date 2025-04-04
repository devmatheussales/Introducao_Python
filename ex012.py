#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoAtual = float(input('Digite o Preço atual: '))
desconto = precoAtual * 0.95
print(f'O novo preço é: {desconto: .2f}')