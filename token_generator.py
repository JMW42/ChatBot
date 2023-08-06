import numpy as np
import pandas as pd

import yaml


unique_words: set = set()
word_files = ["raw data/words_base.txt", "raw data/words_en.txt", "raw data/words_de.txt"] # 


def process_word_file(filepath):
    with open(filepath, "r", encoding='utf-8') as file:
        for line in file.readlines():
            word:str = line.strip().lower()
            unique_words.add(word)

            if len(unique_words) % 1000 == 0:
                print(f'{len(unique_words)}: {word}')
                




for f in word_files:
    print(f"processing word file: {f}")
    process_word_file(f)


wordnums = np.arange(0, len(unique_words), dtype=int)

df = pd.DataFrame({"token":wordnums, "word":list(unique_words)})
df.to_csv("data/tokens_en_de.csv", sep=";", index=False)


print(f"total count of word: {len(unique_words)}")