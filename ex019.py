#Um professor quer sorte um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(f'O Aluno sorteado foi: {escolhido}')
