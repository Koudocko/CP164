import sys,os
sys.path.append(os.path.realpath('../../../wehr6772_data_structures/src'))

from Food import Food
from Food_utilities import *

fh = open("foods.txt", "r")

for food in read_foods(fh):
    print(f"{food}\n")

fh.close()
