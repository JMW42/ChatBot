import pandas as pd

TOKENIZE_SEQUENCE = ["+", "-", "*", ":", ",", "\'", "\"", "#", "°", "^", "?"]


def prepare_line(line):
    """ prepares a line and returns the corresponding wordlist"""
    tmp = line.lower()
    for seq in TOKENIZE_SEQUENCE:
        tmp = tmp.replace(seq, f' {seq} ')

    arr = tmp.split(" ")

    while("" in arr):
        arr.remove("")

    return arr



def tokenize_prepared_line(prepared_line:list, df:pd.DataFrame) -> list:
    """ returns the list of tokens corresponding to the input line"""
    res = []

    for word in prepared_line:
        
        found = df[df["word"] == word]
        if len(found.index) == 0:
            res.append(-1)
        else:
            res.append(found["token"].values[0])


        #if word in tokens:
        #    res.append(tokens.index(word))
        #else:
        #    print("unknown word/token")
        #    res.append(-1)

    return res




def tokenize_line(line:str, df:pd.DataFrame):
    tmp = prepare_line(line)
    return tokenize_prepared_line(tmp, df)