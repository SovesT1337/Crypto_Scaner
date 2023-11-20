import requests
import re
import os


class Etherscan():
    eth_pattern = r'0x[0-9a-f]{40}$'
    url = "https://api.etherscan.io/api?"
    token = os.environ.get('API_Token')
    params_normal = {
                    'module': 'account',
                    'action': 'txlist',
                    'address': '',
                    'apikey': token}
    params_erc = {
                    'module': 'account',
                    'action': 'tokentx',
                    'address': '',
                    'apikey': token}
    

    def check_address(self, name):
        if re.match(self.eth_pattern, name):
            return True
        return False


    def get_addresses(self, address):
        if not self.check_address(address):
            raise ValueError('Неправильно введен адрес')
        self.params_erc['address'] = address
        self.params_normal['address'] = address
        normal = requests.get(self.url, params=self.params_normal)
        if normal.status_code != 200:
            raise Exception('Нет доступа к Etherscan.io методу "txlist"')
        erc = requests.get(self.url, params=self.params_erc)
        if erc.status_code != 200:
            raise Exception('Нет доступа к Etherscan.io методу "tokentx"')
        set_of_adresses = set()

        for element in normal.json()['result']:
            reciever = element['to']
            if reciever != '':
                set_of_adresses.add(reciever)
        
        for element in erc.json()['result']:
            reciever = element['to']
            if reciever != '':
                set_of_adresses.add(reciever)

        return set_of_adresses