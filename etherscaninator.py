import requests
import os


class Ethersvaninator():
    def get_adresses(self, address):
        url = "https://api.etherscan.io/api?"
        token = os.environ.get('API_Token')
        normal = requests.get(url, params={
                                'module': 'account',
                                'action': 'txlist',
                                'address': address,
                                'apikey': token})
        internal = requests.get(url, params={
                                'module': 'account',
                                'action': 'txlistinternal',
                                'address': address,
                                'apikey': token})
        erc = requests.get(url, params={
                                'module': 'account',
                                'action': 'tokentx',
                                'address': address,
                                'apikey': token})
        set_of_adresses = set()
        if normal.status_code == 200:
            for item in normal.json()['result']:
                reciever = item['to']
                if reciever != '':
                    set_of_adresses.add(reciever)
        if internal.status_code == 200:
            for item in internal.json()['result']:
                reciever = item['to']
                if reciever != '':
                    set_of_adresses.add(reciever)
        if erc.status_code == 200:
            for item in erc.json()['result']:
                reciever = item['to']
                if reciever != '':
                    set_of_adresses.add(reciever)
        return set_of_adresses