from urllib import request

url="https://www.wikipedia.org/wiki/principal"
palavra="assassino"

req= request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
resposta=request.urlopen(req)

html=resposta.read().decode("utf-8","ignore")

print(html)
contagem=html.lower().count(palavra.lower())