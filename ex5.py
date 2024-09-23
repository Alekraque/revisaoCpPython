cargo = input('digite seu cargo: ')
salario = float(input('digite seu salario atual: '))
salarioGerente = salario * 0.10 + salario
salarioEngenheiro = salario * 0.20 + salario
salarioTecnico = salario * 0.30 + salario
salarioDesconhecido = salario *0.40 +salario
if cargo == 'gerente':
  print(f'seu salario agora é de R${salarioGerente}')
elif cargo == 'engenheiro':
  print(f'seu salario agora é de R${salarioEngenheiro}')
elif cargo == 'tecnico':
  print(f'seu salario agora é de R${salarioTecnico}')
else:
  print(
    f'se o seu cargo não está aqui, então seu salário recebe 40% de aumento\n\n'
    f'seu salário agora é de R${salarioDesconhecido}'
  )