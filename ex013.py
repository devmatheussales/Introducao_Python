#Faça um algoritmo que leia o salário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário que será reajustado: '))
novoSalario = salario * 1.15
print(f'O novo salário será: {novoSalario: .2f}')