from requests import session
import time
import random
import csv
import pandas


class Dune():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://dune.com/',
        'content-type': 'application/json',
        'Origin': 'https://dune.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
    }
    json_data = {
        'operationName': 'GetExecution',
        'variables': {
            'execution_id': '01HFFDRY9X7BFT6TMQWGZNN6M9',
            'query_id': 2668365,
            'parameters': [],
        },
        'query': 'query GetExecution($execution_id: String!, $query_id: Int!, $parameters: [Parameter!]!) {\n  get_execution(\n    execution_id: $execution_id\n    query_id: $query_id\n    parameters: $parameters\n  ) {\n    execution_queued {\n      execution_id\n      execution_user_id\n      position\n      execution_type\n      created_at\n      __typename\n    }\n    execution_running {\n      execution_id\n      execution_user_id\n      execution_type\n      started_at\n      created_at\n      __typename\n    }\n    execution_succeeded {\n      execution_id\n      runtime_seconds\n      generated_at\n      columns\n      data\n      max_result_size_reached_bytes\n      request_max_result_size_bytes\n      __typename\n    }\n    execution_failed {\n      execution_id\n      type\n      message\n      metadata {\n        line\n        column\n        hint\n        __typename\n      }\n      runtime_seconds\n      generated_at\n      __typename\n    }\n    __typename\n  }\n}\n',
    }
    url = "https://dune.com/sixdegree/starknet-aridrop-simulation-ranking"
    api = 'https://app-api.dune.com/v1/graphql'
    
    
    def __init__(self):
        self.session = session()


    def get_data(self, name):
        file_name = './' + name
        code = self.session.get(self.url, headers = self.headers).status_code
        if code != 200:
            raise Exception('Нет доступа к сервису Dune')
        time.sleep(random.choice([2, 3, 4, 5, 6]))
        response = self.session.post(self.api, headers=self.headers, json=self.json_data)
        if response.status_code != 200:
            raise Exception('Нет доступа к сервису Dune')
        try:
            with open(file_name, 'w') as f:
                writer = csv.DictWriter(f, response.json()['data']['get_execution']['execution_succeeded']['columns'])
                writer.writeheader()
                writer.writerows(response.json()['data']['get_execution']['execution_succeeded']['data'])
        except TypeError:
            raise ('Не удается открыть файл на запись')
        except :
            raise ('Иная ошибка')
        

    def read_ranking_from_csv(self, name):
        file_name = './' + name
        try:
            self.df = pandas.read_csv(file_name)
        except FileNotFoundError:
            raise ('Не удается открыть файл на чтение')
        except :
            raise ('Иная ошибка')
        

    def find_in_ranking(self, list_of_accounts):
        table = self.df[self.df['u'].isin(list_of_accounts)].reset_index()
        del table['index']
        return table
    
