from dune import Dune
from etherscan import Etherscan
import pandas
import pytest
import requests


def test_is_csv_file():
    testing = Dune()
    assert testing.is_csv_file("data.csv") == True
    assert testing.is_csv_file("data.CSV") == True
    assert testing.is_csv_file("Data.Csv") == True
    assert testing.is_csv_file("data.txt") == False
    assert testing.is_csv_file("data") == False
    assert testing.is_csv_file("") == False
    assert testing.is_csv_file(".csv") == False

def test_set_file_name_to_read():
    testing = Dune()
    with pytest.raises(Exception):
        testing.set_file_name_to_read("")
    with pytest.raises(Exception):
        testing.set_file_name_to_read("data.csv")
    with pytest.raises(Exception):
        testing.set_file_name_to_read("data")
    with pytest.raises(Exception):
        testing.set_file_name_to_read(".csv")
    testing.set_file_name_to_read("starknet_users_ranking.csv")
    assert testing.file_to_read == "./starknet_users_ranking.csv"

def test_set_file_name_to_write():
    testing = Dune()
    with pytest.raises(Exception):
        testing.set_file_name_to_write("")
    with pytest.raises(Exception):
        testing.set_file_name_to_write("data")
    with pytest.raises(Exception):
        testing.set_file_name_to_write(".csv")
    testing.set_file_name_to_write("starknet_users_ranking.csv")
    assert testing.file_to_write == "./starknet_users_ranking.csv"

def test_get_data():
    # Не совсем понимаю какие тесты сюда можно написать. 
    # Ну наверное стоит сюда написать проверку того что создался файл. 
    # Но там немного не понятно, потому что его тогда каждый раз удалять надо
    testing = Dune()
    with pytest.raises(TypeError):
        testing.get_data()
    testing.api = ""
    with pytest.raises(Exception):
        testing.get_data()
    testing.headers = {}
    with pytest.raises(Exception):
        testing.get_data()

def test_read_ranking_from_csv():
    testing = Dune()
    with pytest.raises(TypeError):
        testing.read_ranking_from_csv()
    testing.file_to_read = 'starknes_ranking.csv'
    with pytest.raises(TypeError):
        testing.read_ranking_from_csv()
    testing.file_to_read = 'starknet_users_ranking.csv'
    testing.read_ranking_from_csv()
    assert type(testing.df) == pandas.DataFrame

def test_find_in_ranking():
    testing = Dune()
    testing.file_to_read = 'starknet_users_ranking.csv'
    testing.read_ranking_from_csv()
    to_check = testing.find_in_ranking(["0x74c4aed579cd7bd50d503154380feee75c2fe6ca"])
    assert type(to_check) == pandas.DataFrame
    assert to_check.loc[193].at["u"] == "0x74c4aed579cd7bd50d503154380feee75c2fe6ca"
    to_check = testing.find_in_ranking(["0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"])
    assert type(to_check) == pandas.DataFrame
    assert to_check.empty

def test_check_address():
    testing = Etherscan()
    assert testing.check_address("0xc7d688cb053c19ad5ee4f48c348958880537835f") == True
    assert testing.check_address("") == False
    assert testing.check_address("32a992c20e0c0d5d556db339c3fa5eef3b5bbd52") == False
    assert testing.check_address("0x3c20e0c0d5d556db339c3fa5eef3b5bbd52") == False
    assert testing.check_address("0x3c20e0c0d5d556db339c3fa5eef3b5bbав2") == False
    assert testing.check_address("0x3c20e0c0d5d556db339c3fa5eef3b5bb//2") == False

def test_get_address():
    testing = Etherscan()
    with pytest.raises(ValueError):
        testing.get_addresses("sdafhjah")
    with pytest.raises(ValueError):
        testing.get_addresses("")
    # Если запускать через командную строку, последний тест почему-то не проходит :(
    assert type(testing.get_addresses("0x74c4aed579cd7bd50d503154380feee75c2fe6ca")) == set

if __name__ == "__main__":
    pytest.main()
