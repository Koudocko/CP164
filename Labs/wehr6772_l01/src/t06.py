import sys,os
sys.path.append(os.path.realpath('../../../wehr6772_data_structures/src'))

from Food import Food
from Food_utilities import *

fh_old, fh_new = open("foods.txt", "r"), open("new_foods.txt", "w")

write_foods(fh_new, read_foods(fh_old))

fh_old.close()
fh_new.close()
