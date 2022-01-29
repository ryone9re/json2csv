from sys import argv
from json import loads

from pandas import json_normalize

with open(argv[1], 'r') as f:
    data = f.read()
    j = loads(data)
    df = json_normalize(j)
    df.to_csv("output.csv")
