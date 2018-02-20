import yaml
import random

my_dict = yaml.load(open("files/test.yaml", "r", encoding="utf-8"))


print(random.choice(list(my_dict['opponents'].keys())))