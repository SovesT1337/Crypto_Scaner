from starkterractor import Starkterrator
from etherscaninator import Ethersvaninator

if __name__ == "__main__":
    shit1 = Starkterrator()
    shit1.get_data()
    shit1.read_ranking_from_csv()
    shit2 = Ethersvaninator()
    address = ''
    while address != 'q':
        address = input("Введите интересующий вас адрес: ")
        set_of_addresses = shit2.get_adresses(address)
        print(shit1.find_in_ranking(list(set_of_addresses)))