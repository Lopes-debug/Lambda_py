# dicionario = {'vinho':540, 'cerveja':320, 'coca':642, 'pepsi':100}

# aplicar uma função rapidamente em apenas uma linha de codigo usando map
# lambida = list(map(lambda num: num*2, dicionario.values()))
# print(lambida)

# aplicar lambda dentro de uma função
# def calcular_imposto(imposto):
#     return lambda preco: preco * (1 + imposto)

# produto 0.1
#serviço 0.15
#royalties 0.25

# calcular_preco_produto = calcular_imposto(0.1)
# calcular_preco_servico = calcular_imposto(0.15)
# calcular_preco_royalties = calcular_imposto(0.25)

# print(int(calcular_preco_produto(100))) 
# print(int(calcular_preco_servico(100)))
# print(calcular_preco_royalties(100))
