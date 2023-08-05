import numpy as np
import pandas as pd

import yaml


file = open('data/train_ambignq_light.yaml', 'r')
knowledge = yaml.load(file)


def clear_from_special_chars(line):
    return line.replace(".", " . ").replace("?", " ?").replace("!", " !").replace("(", "").replace(")", "").replace(", ", " ").replace("\"", "")





def iterate_over_words(entry):

    inp = clear_from_special_chars(entry["input"])
    resp = entry["response"]

    words = inp.split(" ")

    for r in resp:
        r2 = clear_from_special_chars(r).split(" ")
        words = words + r2

    words = list(set(words))

    return words




count = 0

unique_words = []

for entry in knowledge:
    words = iterate_over_words(entry)

    for word in words:
        if word not in unique_words:
            unique_words.append(word)
            print(f"\t {count}: {word}")
            count += 1
        

df = pd.DataFrame({"word":unique_words})
df["token"] = list(range(0, len(df["word"].values)))
df["token"] = df["token"].astype("int")

print(f"In total {count} words discovered")

df.to_csv("data/tokens.csv", sep=";", index=False)