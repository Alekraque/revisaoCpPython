#fazendo os códigos de acordo com o conteudo das aulas
codigo = input("Informe o código do produto (1001, 1324, 6548, 0987, 7623): ")
quantidade = int(input("Informe a quantidade comprada: "))

if codigo == '1001':
    precoUni = 5.32
    percentualImposto = 0.18
elif codigo == '1324':
    precoUni = 6.45
    percentualImposto = 0.18
elif codigo == '6548':
    precoUni = 2.37
    percentualImposto = 0.06
elif codigo == '0987':
    precoUni = 5.32
    percentualImposto = 0.06
elif codigo == '7623':
    precoUni = 6.45
    percentualImposto = 0.12
else:
    print("Código de produto inválido.")

valorPago = precoUni * quantidade
imposto = valorPago * percentualImposto
valorTotal = valorPago + imposto

print(
  f"Valor pago por cada produto: R$ {valorPago:.2f}\n"
  f"Valor do imposto: R$ {imposto:.2f}\n"
  f"Imposto total: R$ {imposto:.2f}\n"
  f"Valor total a ser pago: R$ {valorTotal:.2f}"

)
