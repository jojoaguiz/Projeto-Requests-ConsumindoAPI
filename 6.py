import requests

url = 'https://68c96217ceef5a150f649e8c.mockapi.io/Restaurante2'
resposta = requests.get(url)
pedidos = resposta.json()

print("Pedidos já feitos:")
for pedido in pedidos:
    print(f"ID: {pedido['id']} | Prato: {pedido.get('prato', pedido.get('parto'))} | Bebida: {pedido.get('bebida')} | Mesa: {pedido.get('mesa')}")

id_excluir = input("Digite o ID do pedido que deseja excluir: ")

url_excluir = f"{url}/{id_excluir}"
resposta_excluir = requests.delete(url_excluir)

if resposta_excluir.status_code == 200:
    print("Pedido excluído com sucesso!")
else:
    print("Erro ao excluir o pedido.")