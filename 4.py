import requests

url = "https://68c96217ceef5a150f649e8c.mockapi.io/Restaurante2"  
dados = {"pedido": "Pizza"}

resposta = requests.post(url, json=dados)

print("Status:", resposta.status_code)
print("Resposta da API:", resposta.text)