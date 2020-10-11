from django.shortcuts import render


def home(request):
    import requests
    import json

    #Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,XRP,BCH,BNB,LINK,DOT&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    # Crypto News API
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json

        quote = request.POST['quote']
        quote = quote.upper()
        value_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        value = json.loads(value_request.content)
        return render(request, 'prices.html', {'quote': quote, 'value':value})

    else:
        notfound = "Enter a valid crypto currency name into the form..."
        return render(request, 'prices.html', {'notfound': notfound})
