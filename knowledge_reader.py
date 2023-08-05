import yaml


file = open("data/train_ambignq_light.yaml", "r")
knowledge = yaml.load(file)

for entry in knowledge:
    print(entry)
    break