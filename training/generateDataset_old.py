# Convert a .json dataset to a .csv dataset

import json
import pandas as pd

DATASET_PATH = 'dataset/train-v2.0.json'

# Load the dataset file
with open(DATASET_PATH) as json_file:
    data = json.load(json_file)
    data = data['data']

    # Create a DataFrame to store the data
    df = pd.DataFrame(columns=['context', 'question', 'answer', 'answer_start', 'answer_end'])
    count = 0
    for article in data:
        count += 1
        print(f"{(count / len(data) * 100):.2f}%")
        for paragraph in article['paragraphs']:
            context = paragraph['context']
            for qa in paragraph['qas']:
                question = qa['question']
                for answer in qa['answers']:
                    answer_text = answer['text']
                    answer_start = answer['answer_start']
                    answer_end = answer_start + len(answer_text)
                    df = pd.concat([df, pd.DataFrame.from_records([{'context': context, 'question': question, 'answer': answer_text, 'answer_start': answer_start, 'answer_end': answer_end}])])

    # Save the DataFrame to a CSV file
    df.to_csv('dataset/train.csv', index=False)

print("Done.")
print("Preview:")
print(df.head())
