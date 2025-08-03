import pandas as pd
from random import randint

s = randint(0,101)
a = pd.read_csv("data/french_words.csv")
b = a.to_dict(orient="records")
c = b[s]["English"]
print(b)
b.pop(s)
print(b[s])
print(b)