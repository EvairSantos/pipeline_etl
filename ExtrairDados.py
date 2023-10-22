import requests

# URL da API CoinGecko para o Bitcoin
url = "https://api.coingecko.com/api/v3/simple/price"

# Parâmetros da consulta
params = {
    "ids": "bitcoin",
    "vs_currencies": "usd"
}

# Realiza a consulta
response = requests.get(url, params=params)

if response.status_code == 200:
    bitcoin_data = response.json()
    price_in_usd = bitcoin_data['bitcoin']['usd']
    print(f"Preço atual do Bitcoin (em USD): {price_in_usd}")
else:
    print("Falha ao obter os dados.")
