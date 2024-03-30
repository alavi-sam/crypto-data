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
        pass


    def get_spot(self, date=None):
        pass
