import requests
from datetime import datetime, timedelta
from time import sleep

# Criando por quanto tempo será rodado o script, no caso 15 minutos
tempo_final = datetime.now() + timedelta(hours=24)

# Realizando o loop
while True:
    if datetime.now() >= tempo_final:
        print(f'Fim do script')
        break
    else:
        # Realizando a requisição na API
        cotacao = requests.get(
            'https://economia.awesomeapi.com.br/last/USD-BRL,GBP-BRL,NOK-BRL,BTC-BRL,NZD-BRL,CHF-BRL,ETH-BRL,DKK-BRL,'
            'COP-BRL,RUB-BRL,CNY-BRL,INR-BRL,MXN-BRL,PLN-BRL,EUR-BRL,SAR-BRL,TRY-BRL,PYG-BRL,AED-BRL,HKD-BRL,'
            'XRP-BRL,ZAR-BRL,USD-BRL,CAD-BRL,JPY-BRL,ILS-BRL,SGD-BRL,SEK-BRL,THB-BRL,PEN-BRL,DOGE-BRL,TWD-BRL,'
            'LTC-BRL,AUD-BRL,CLP-BRL,BOB-BRL,ARS-BRL,UYU-BRL')
        todas_moedas = cotacao.json()

        # Definição do horário da busca
        horario_atual = datetime.now()
        horario_atual = horario_atual.strftime('%d/%m/%Y %H:%M:%S')

        # Imprimindo as informações
        print(f'Hora da análise {horario_atual}')
        for n in todas_moedas.values():
            print(f"{n.get('code')}: {n.get('name')} vale R$ {n.get('bid')}")
        print('*' * 40)
        print()
        sleep(600)
