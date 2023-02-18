import requests



api_key = "90cd9764bfafe98ea79989a4e40840ee"

nome_capital = str(input("Qual a capital que você deseja ver a temperatura: "))

link = f"https://api.openweathermap.org/data/2.5/weather?q={nome_capital}&appid={api_key}&lang=pt_br"


requisicao = requests.get(link)



requisicao.json()

requisicao_dic = requisicao.json()

descricao = requisicao_dic ['weather'][0]['description']


temperatura = int(requisicao_dic ['main']['temp'] - 273.15)



print(f"Em {nome_capital}, está {temperatura} ºC, {descricao}")