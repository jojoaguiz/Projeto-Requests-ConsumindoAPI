import requests

pedido = {
    'bebida': input('Qual a bebida? ').upper(),
    'prato': input('Qual o prato? ').upper(),
}

resposta = requests.post('https://68c96217ceef5a150f649e8c.mockapi.io/Restaurante2',json=pedido)

print("Status:", resposta.status_code)
print("Resposta da API:", resposta.text)
