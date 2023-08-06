import numpy as np
import pandas as pd


df = pd.read_csv("data/tokens.csv", sep=";")
token = list(df["word"].values)



while True:
    print("-"*80)
    inp = input(">")
    if inp == "exit": break

    tmp = inp.split(" ")
    print(tmp)

    tokenized = []

    for wd in tmp:
        if wd in token:
            tokenized.append(token.index(wd))
        else:
            print("unknown word/token")
            tokenized.append(-1)

    print(tokenized)