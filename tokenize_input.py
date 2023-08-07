import numpy as np
import pandas as pd

import modules.tokentools as toktools

df = pd.read_csv("data/tokens_en_de.csv", sep=";")
tokens = list(df["word"].values)



while True:
    print("-"*80)
    inp = input(">")
    if inp == "exit": break

    tmp = toktools.prepare_line(inp)
    print(tmp)

    tokenized = toktools.tokenize_line(tmp, tokens)

    print(tokenized)