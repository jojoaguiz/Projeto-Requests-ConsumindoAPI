import requests

resposta1=requests.get('https://catfact.ninja/fact')
fato1=resposta1.json()

resposta2=requests.get('https://catfact.ninja/fact')
fato2=resposta2.json()


print("O primeiro gato tem :",fato1.get('length'))
print("O segundo gato tem :",fato2.get('length'))

if fato1.get('length') > fato2.get('length'):
    print('O primeiro é maior')
else:
    print('O segundo é maior')