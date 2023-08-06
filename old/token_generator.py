import numpy as np
import pandas as pd

import yaml


file = open('data/train_ambignq_light.yaml', 'r')
knowledge = yaml.load(file)


def clear_line(line):
    tmp = line.lower()
    tmp = tmp.replace(".", " . ").replace("?", " ?").replace("!", " !").replace("(", " ").replace(")", " ").replace(", ", " ").replace("\"", "").replace("-", " ")

    tmp = tmp.replace("/", " ").replace(",", " ").replace("\t", " ").replace("\n", " ")

    return tmp.split("|")[0]


def clear_word_list(words):
    while "" in words:
        words.remove("")

    return words


def iterate_over_words(entry):

    inp = clear_line(entry["input"])
    resp = entry["response"]

    words = clear_word_list(inp.split(" "))

    for r in resp:
        r2 = clear_line(r).split(" ")
        words = words + clear_word_list(r2)

    words = list(set(words))

    return words



count = 0
unique_words = []


def tokenize_word(word):
    global count, unique_words
    if word not in unique_words:
        unique_words.append(word)
        print(f"\t {count}: {word}")

        if len(word) >= 20:
            print("LONG WORD !!!")
            input()

        count += 1
        return True
    else:
        return False


# tokenize ascii characters:
for i in range(255):
    tokenize_word(chr(i))


# tokenize some important numbers:
for i in range(4000):
    tokenize_word(str(i))


# tokenize knowledge:

for entry in knowledge:
    words = iterate_over_words(entry)

    for word in words:
         tokenize_word(word)




df = pd.DataFrame({"word":unique_words})
df["token"] = list(range(0, len(df["word"].values)))
df["token"] = df["token"].astype("int")

print(f"In total {count} words discovered")

df.to_csv("data/tokens.csv", sep=";", index=False)