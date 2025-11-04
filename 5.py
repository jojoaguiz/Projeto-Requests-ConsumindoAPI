import requests

pedido={
    'parto':'Lasanha',
    'bebida':'Suco de Laranja',
    'mesa':'7',
}

requests.put('https://68c96217ceef5a150f649e8c.mockapi.io/Restaurante2', pedido)

