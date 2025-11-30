import os
import re

data_dir = os.listdir('data')

year_ans = set()

for data in data_dir:
    dataset_path = os.listdir(f"data/{data}")
    for filename in dataset_path:
        with open(os.path.join(f'data/{data}', filename), 'r') as file:
            content = file.read()
            if re.search(r"\[\[Number of people: [0-9]*\]\]", content):
                print(data)
                break
