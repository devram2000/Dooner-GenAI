import PyPDF2
import os
from tqdm import tqdm

# Folder containing your PDFs (in the current directory)
pdf_folder = './Sustainability Plans'

# Corpus to store all texts
corpus = []

# List of PDF files
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

# Iterate over each PDF file in the folder with a progress bar
for filename in tqdm(pdf_files, desc='Processing PDFs', unit='pdf'):
    file_path = os.path.join(pdf_folder, filename)

    # Append the title (filename without extension)
    title = os.path.splitext(filename)[0]
    corpus.append(f"Title: {title}\n" + "-"*40 + "\n")

    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Extract text from each page and add to the corpus
        for page in reader.pages:
            text = page.extract_text()
            if text:  # Only add non-empty text
                cleaned_text = ''.join(char for char in text if char.isprintable())
                corpus.append(cleaned_text)
        
        # Add a separator after each PDF's text
        corpus.append("\n" + "-"*40 + "\n")

# Save the corpus to a file
with open('corpus.txt', 'w', encoding='utf-8') as corpus_file:
    for text in corpus:
        corpus_file.write(text + '\n')

print("All PDFs processed. Corpus saved to 'corpus.txt'.")
