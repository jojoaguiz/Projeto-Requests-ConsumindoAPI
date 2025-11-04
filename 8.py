
import requests

pedido1 = {
    'Prato': 'Pizza Margherita',
    'Bebida': 'Coca-Cola',
    'Mesa': 1,
}
pedido2 = {
    'Prato': 'Hambúrguer Suculento',
    'Bebida': 'Suco de Laranja',
    'Mesa': 2,
}
pedido3 = {
    'Prato': 'Feijoada Tradicional',
    'Bebida': 'Água Mineral',
    'Mesa': 3,
}
pedido4 = {
    'Prato': 'Pizza Margherita',
    'Bebida': 'Coca-Cola',
    'Mesa': 4,
}
pedido5 = {
    'Prato': 'Hambúrguer Suculento',
    'Bebida': 'Coca-Cola',
    'Mesa': 5,
}



posts = [pedido1, pedido2, pedido3, pedido4, pedido5]

url = 'https://68c96217ceef5a150f649e8c.mockapi.io/Restaurante2'


novo_pedido = {
    'Prato': input("Digite o prato: "),
    'Bebida': input("Digite a bebida: "),
    'Mesa': int(input("Digite o número da mesa: "))
}
resposta = requests.post(url, json=novo_pedido)






resposta_get = requests.get(url)
pedidos = resposta_get.json()
print("\nPedidos existentes:")
for pedido in pedidos:
    print(f"ID: {pedido['id']} | Mesa: {pedido['Mesa']} | Prato: {pedido['Prato']} | Bebida: {pedido['Bebida']}")

id_apagar = input("\nDigite o ID do pedido que deseja apagar: ")
url_delete = f"{url}/{id_apagar}"
resposta_delete = requests.delete(url_delete)
if resposta_delete.status_code == 200:
    print("Pedido apagado com sucesso!")
else:
    print("Erro ao apagar o pedido.")

resposta_get = requests.get(url)
pedidos = resposta_get.json()
print("\nPedidos existentes:")
for pedido in pedidos:
    print(f"ID: {pedido['id']} | Mesa: {pedido['Mesa']} | Prato: {pedido['Prato']} | Bebida: {pedido['Bebida']}")

id_atualizar = input("\nDigite o ID do pedido que deseja atualizar: ")
url_put = f"{url}/{id_atualizar}"
pedido_atualizado = {
    'Prato': input("Digite o novo prato: "),
    'Bebida': input("Digite a nova bebida: "),
    'Mesa': int(input("Digite o novo número da mesa: "))
}
resposta_put = requests.put(url_put, json=pedido_atualizado)
if resposta_put.status_code == 200:
    print("Pedido atualizado com sucesso!")
else:
    print("Erro ao atualizar o pedido.")
