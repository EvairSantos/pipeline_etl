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
    
    # Vamos supor que estamos fazendo uma análise simples da tendência.
    # Se o preço do Bitcoin for maior do que o valor anterior, consideramos uma tendência de alta.
    # Caso contrário, consideramos uma tendência de baixa.
    
    # Aqui você pode comparar o preço atual com um valor anterior
    # que você coletou durante a extração.
    
    valor_anterior = 80000  # Substitua pelo valor anterior da extração.
    
    if price_in_usd > valor_anterior:
        print("Tendência: Alta")
    else:
        print("Tendência: Baixa")
    
else:
    print("Falha ao obter os dados.")
