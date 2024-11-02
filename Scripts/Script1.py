#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

lista = []

aluno = {}

while True:
    aluno['nome'] = str(input('nome: '))
    aluno['nota1'] = float(input('primeira nota: '))
    aluno['nota2'] = float(input('segunda nota: '))
    aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
    if aluno['media'] > 7:
        aluno['estado'] = str('Aprovado')
    else:
        aluno['estado'] = str('Reprovado')
    lista.append(aluno.copy())

    op = str(input('deseja continuar [S/N]? ')).strip().upper()
    if 'N' in op:
        break

print(lista)
