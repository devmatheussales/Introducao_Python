#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem de aprensetação será: {lista}')
