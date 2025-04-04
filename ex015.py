#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro cursta R$60,00 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos Dias o Carro foi alugado? '))
hodometro = float(input('Quantos KMs o carro rodou? '))

preco = (dias * 60) + (hodometro * 0.15)
print(f'O valor a pagar é de R$:{preco}')
