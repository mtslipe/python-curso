#Exercício Python #010 - Conversor de Moedas

import requests

# Pega a cotação do dólar usando uma API pública
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
resposta = requests.get(url)
dados = resposta.json()


cotacao_dolar = float(dados['USDBRL']['bid'])
print(f"Cotação atual do dólar: R${cotacao_dolar:.2f}")

din = float(input("Digite o valor em reais: R$"))
dolar = din / cotacao_dolar

print(f"Com R${din:.2f} você pode comprar ${dolar:.2f} dólares")