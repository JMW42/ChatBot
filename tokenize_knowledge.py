import numpy as np
import pandas as pd

import modules.tokentools as toktools

import yaml


file_knowledge = open("data/train_ambignq_light.yaml", "r")
knowledge = yaml.load(file_knowledge)


df = pd.read_csv("data/tokens_en_de.csv", sep=";")
tokens = list(df["word"].values)


tokenize_knowledge = []


for entry in knowledge:
    print(entry)

    inp = toktools.tokenize_line(entry["input"], df)
    print(inp)
    
    resp = []
    for r in entry["response"]:
        resp.append(toktools.tokenize_line(r, df))

    print(resp)


    tokenize_knowledge.append({"inpt":inp, "resp":resp})

file = open("data/train__tokenized_ambignq_light.yaml.yaml", "w", encoding='utf-8')

yaml.dump(tokenize_knowledge, file)