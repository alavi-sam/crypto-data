import requests



class Crypto:
    def __init__(self, base, currency):
        self.currency = currency
        self.base = base


    def get_sell(self, date=None):
        if date:
            res = requests.get(f'https://api.coinbase.com/v2/prices/{self.base}-{self.currency}/sell?date={date}')
        else:
            res = requests.get(f'https://api.coinbase.com/v2/prices/{self.base}-{self.currency}/sell')
        return res.json()


    def get_buy(self, date=None):
        if date:
            res = requests.get(f'https://api.coinbase.com/v2/prices/{self.base}-{self.currency}/buy?date={date}')
        else:
            res = requests.get(f'https://api.coinbase.com/v2/prices/{self.base}-{self.currency}/buy')
        return res.json()



    def get_spot(self, date=None):
        if date:
            res = requests.get(f'https://api.coinbase.com/v2/prices/{self.base}-{self.currency}/spot?date={date}')
        else:
            res = requests.get(f'https://api.coinbase.com/v2/prices/{self.base}-{self.currency}/spot')
        return res.json()

