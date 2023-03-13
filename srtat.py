""" something"""
from typing import Type, Union
from athlete import Athlete

def agregation(element_1: Union[str, int], element_2: Union[str, int]):
    """ Create an agregation with two elements
    :param - element_1: string with first element
           - element_2: string with second element
    :return - string with elements agregated
    """
    return element_1 + element_2

def receive_athlete(athlete: Type[Athlete]):
    print(athlete)