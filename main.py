from dune import Dune
from etherscan import Etherscan

if __name__ == "__main__":
    starknet = Dune()
    file_name = 'starknet_users_ranking.csv'
    # file_name = input("Введите название файла: ")       
    try: 
        # starknet.get_data(file_name)
        starknet.read_ranking_from_csv(file_name)
    except Exception:
        print("Что-то пошло не так при открытии файла или загрузке информации")

    ether = Etherscan()
    address = ''
    while address != 'q':
        try:
            address = input("Введите интересующий вас адрес: ")
            set_of_addresses = ether.get_addresses(address)
            to_check = starknet.find_in_ranking(list(set_of_addresses))
            print(to_check)
        except:
            print("Что-то пошло не так при поиске аккаунтов")