from dune import Dune
from etherscan import Etherscan
import pandas
import pytest


def test_get_data():
    testing = Dune()
    with pytest.raises(TypeError):
        testing.get_data('starknet_uss_rankisv')
    testing.api = ""
    with pytest.raises(Exception):
        testing.get_data('starknet_users_ranking.csv')
    testing.headers = {}
    with pytest.raises(Exception):
        testing.get_data('starknet_users_ranking.csv')

def test_read_ranking_from_csv():
    testing = Dune()
    with pytest.raises(TypeError):
        testing.read_ranking_from_csv("")
    with pytest.raises(TypeError):
        testing.read_ranking_from_csv("starkneers_ranking.csv")
    testing.read_ranking_from_csv("starknet_users_ranking.csv")
    assert type(testing.df) == pandas.DataFrame

def test_find_in_ranking():
    testing = Dune()
    testing.read_ranking_from_csv('starknet_users_ranking.csv')
    to_check = testing.find_in_ranking(["0x74c4aed579cd7bd50d503154380feee75c2fe6ca"])
    assert type(to_check) == pandas.DataFrame
    assert not to_check.empty
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
