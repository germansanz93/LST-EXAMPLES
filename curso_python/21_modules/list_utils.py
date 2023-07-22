from random import random
from math import floor

def choose_random_element(list):
    length = len(list)
    rand_index = floor(random() * length)
    return list[rand_index]

