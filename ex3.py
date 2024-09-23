#fazendo os códigos de acordo com o conteudo das aulas

velocidade = int(input('a quantos km/h você estava: '))
multa = 5
excesso = velocidade - 80
if velocidade > 80:
  print('você foi multado em 5 reais por cada km/h que você ultrapassou\n'
  f'portanto, sua multa ficou em {excesso * multa}')
else: 
  print('você não excedeu o limite da rodovia')