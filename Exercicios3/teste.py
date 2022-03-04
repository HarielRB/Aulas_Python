farmacia = ['banana', 'maçã', 'pera']
ordem_pedido = []
ordem_pedido.append(farmacia[:])
print(ordem_pedido)
ordem_pedido[0][0] = 'uva'
print(ordem_pedido)
print(farmacia)