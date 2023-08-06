import yaml, random
from difflib import get_close_matches

filepath = "data/train_ambignq.yaml"
file = open(filepath, "r")

knowledge = yaml.load(file)
knowledge_input = []

for entry in knowledge:
    knowledge_input.append(entry['input'])


while True:
    inp = input("> ")

    if inp == "exit":
        break

    # chatbot response generator

    found = get_close_matches(inp, knowledge_input, n=1, cutoff=0.8)
    
    if found == []:
        match = None
    else:
        match = found[0]

    response = "unknwon question"

    for entry in knowledge:
        if entry["input"] == match:
            response = random.choice(entry["response"])
            break
    
    print(f"\t INPUT: {inp}")
    print(f"\t FOUND: {match}")
    print(f"\t RESPONSE: {response}")

print("EXIT")