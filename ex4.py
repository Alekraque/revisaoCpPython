#fazendo os códigos de acordo com o conteudo das aulas

aluno = input('qual é o aluno em questão: ')
n1 = int(input('qual a 1° nota: '))
n2 = int(input('qual a 2° nota: '))
n3 = int(input('qual a 3° nota: '))
me = (n1+n2+n3)/3
ma = (n1 + n2 * 2 + n3 * 3 + me )/7

print(
  f'ALUNO IDENTIFICADO COMO: {aluno}\n\n'
  f'notas:\n 1°: {n1}\n 2°: {n2}\n 3°: {n3}\n\n'
  f' média: {me}\n\n'
  f'média de aproveitamento: {ma:.2f}'
  

)
