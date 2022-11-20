# Convert a .json dataset to a .csv dataset

import json
import pandas as pd

DATASET_PATH = 'dataset/train-v2.0.json'

# Load the dataset file
with open(DATASET_PATH) as json_file:
    data = json.load(json_file)
    data = data['data']

    # Create a DataFrame to store the data
    df = pd.DataFrame(columns=["source", "target"])
    count = 0
    for article in data:
        count += 1
        print(f"{(count / len(data) * 100):.2f}%")
        for paragraph in article['paragraphs']:
            context = paragraph['context']

            source_question = "generate question: " + context
            target_question = ""
            source_answer = "extract answer: <hl> " + context + " </hl>"
            target_answer = ""

            ignore_answers = []

            for qa in paragraph['qas']:
                question = qa['question']
                if len(qa['answers']) > 0:
                    answer = qa['answers'][0]
                    answer_text = answer['text']

                    if answer_text in ignore_answers:
                        continue

                    source_question = source_question.replace(answer_text, "<hl> " + answer_text + " </hl>", 1)
                    target_question += question + " <sep> "

                    target_answer += answer_text + " <sep> "

                    ignore_answers.append(answer_text)

                    # answer_start = answer['answer_start']
                    # answer_end = answer_start + len(answer_text)
                    # df = pd.concat([df, pd.DataFrame.from_records([{'context': context, 'question': question, 'answer': answer_text, 'answer_start': answer_start, 'answer_end': answer_end}])])

            df = pd.concat([df, pd.DataFrame.from_records([{"source": source_answer, "target": target_answer}])])
            df = pd.concat([df, pd.DataFrame.from_records([{"source": source_question, "target": target_question}])])

    # Save the DataFrame to a CSV file
    df.to_csv('dataset/train_test.csv', index=False)

print("Done.")
print("Preview:")
print(df.head())
