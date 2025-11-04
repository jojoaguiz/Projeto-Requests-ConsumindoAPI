import requests
pedido={
'bebida':'Refrigerante',
'mesa':'7',
'prato':'Lasanha',
}
requests.post('https://68c96217ceef5a150f649e8c.mockapi.io/Restaurante',pedido)
