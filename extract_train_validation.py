from pdfminer.high_level import extract_text
import os
import json
import random
from tqdm import tqdm

# Further reduce the token limit per example
MAX_CHARS = 12000  # Approximate character limit based on token limit

def clean_text(text):
    return text  # Implement cleaning logic as needed

def check_and_split_text(text, max_chars):
    for i in range(0, len(text), max_chars):
        yield text[i:i + max_chars]

# Folder containing your PDFs
pdf_folder = './Sustainability Plans'

all_data = []

pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
for filename in tqdm(pdf_files, desc='Processing PDFs', unit='pdf'):
    file_path = os.path.join(pdf_folder, filename)

    text = extract_text(file_path)
    if text:
        cleaned_text = clean_text(text)
        for part in check_and_split_text(cleaned_text, MAX_CHARS):
            data = {
                "messages": [
                    {"role": "system", "content": "The assistant provides sustainability plans."},
                    {"role": "user", "content": f"Provide a sustainability plan for {os.path.splitext(filename)[0].replace('_', ' ')}."},
                    {"role": "assistant", "content": part}
                ]
            }
            all_data.append(data)

random.shuffle(all_data)
split_index = int(len(all_data) * 0.8)
training_data = all_data[:split_index]
validation_data = all_data[split_index:]

with open('training_data.jsonl', 'w') as file:
    for item in training_data:
        file.write(json.dumps(item) + '\n')

with open('validation_data.jsonl', 'w') as file:
    for item in validation_data:
        file.write(json.dumps(item) + '\n')
