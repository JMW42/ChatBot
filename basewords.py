


# append ascii characters:

words = []


def add_word(word):
    if not word in words:
        words.append(word)



for i in range(0, 4001):
    add_word(str(i))

for i in range(0, 255):
    add_word(chr(i))


file = open("raw data/words_base.txt", "w", encoding='utf-8')


for w in words:
    print(f'{w}')
    file.write(f'{w}\n')


file.close()