#fazendo os códigos de acordo com o conteudo das aulas

peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura em metros: '))

imc = peso / (altura * altura)

if imc < 18.5:
  print(f' seu IMC é: {imc}\nseu peso está abaixo do esperado')
elif imc > 18.5 and imc < 25:
  print(f'seu IMC é: {imc}\nseu peso está normal')
elif imc >= 25 and imc < 30:
  print(f'seu IMC é: {imc}\nvocê está em excesso de peso')
elif imc >= 30 and imc < 35:
  print(f'seu IMC é: {imc}\nvocê está com obesidade de Grau I')
elif imc >= 35 and imc < 40:
  print(f'seu IMC é: {imc}\nvocê está com Obesidade Grau II')
else: 
  print(f'seu IMC é: {imc}\nvocê está com Obesidade Mórbida')