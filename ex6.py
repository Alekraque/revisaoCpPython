#fazendo os códigos de acordo com o conteudo das aulas
pessoas = int(input("Informe a quantidade de pessoas na casa: "))
minPorPessoa = int(input("Informe a quantidade média de minutos que cada pessoa demora no banho: "))
potenciaChuveiro = 2400
consumoPorDiaKwh = (potenciaChuveiro / 1000) * (minPorPessoa * pessoas / 60)
consumoPorMesKwh = consumoPorDiaKwh * 30
custoTotal = consumoPorMesKwh * 0.40
print(
  f'Consumo total em kWh no mês: {consumoPorMesKwh:.2f} kWh\n\n'
  f'Valor gasto em reais: R$ {custoTotal:.2f}'
)
