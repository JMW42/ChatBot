import json, yaml

file = open("raw data/ambignq/train.json", "r")

data = json.load(file)

knowledge = []


count = 1

for entry in data:
    question: str = entry['question']
    answer: list = ['<answer unkown>']

    if entry['annotations'][0]['type'] == 'singleAnswer':
        answer = entry['annotations'][0]['answer']
        count += 1
    
        knowledge.append({"input":question, 'response':answer})
        print(f'{count}: {question}')
        print(f'\t => {answer}')

    if entry['annotations'][0]['type'] == 'multipleQAs':
        for e in entry['annotations'][0]['qaPairs']:
            count += 1
            question = e['question']
            answer = e['answer']
            knowledge.append({"input":question, 'response':answer})
            print(f'{count}: {question}')
            print(f'\t => {answer}')
            
    
    


with open('data/train_ambignq.yaml', 'w') as outfile:
    yaml.dump(knowledge, outfile, default_flow_style=False)

#file2 = open("data/train_ambignq_light.json", "w")
#f = json.dump(data, file2, indent=4)


#print(f)
