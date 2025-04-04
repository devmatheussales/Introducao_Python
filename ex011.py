#Faça um programa que leia a altura e a largura de uma parede, calcule a sua área e a quantidade de tinta necessárria para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a largura em metros: '))

metrosQuadrados = altura * largura
quantidadeTinta = metrosQuadrados / 2
print(f'Para pintar {metrosQuadrados}m², serão necessários {quantidadeTinta}Litros de tinta')
