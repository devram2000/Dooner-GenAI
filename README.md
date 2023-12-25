# Generative AI SJU Sustainability Plan Project Repository

## Overview
This repository hosts a collection of Python scripts integral to creating the Saint John's University (SJU) Sustainability Plan. The centerpiece, `api_model.py`, interfaces with the OpenAI API to generate the plan's content. Additional scripts offer functionalities like text extraction, summarization, interactive GPT interface, and PDF formatting.

## Scripts Description

### `api_model.py`
- **Purpose**: Automates the generation of the SJU Sustainability Plan text via OpenAI's GPT model.
- **Requirements**:
  - Python 3.x
  - OpenAI Python SDK (`pip install openai`)
  - An OpenAI API key set as an environment variable
- **Environment Variable Setup**:
  - Obtain an OpenAI API key from the OpenAI website.
  - Set the API key as an environment variable:
    - On Linux/Mac: `export OPENAI_API_KEY='your-api-key'`
    - On Windows: `set OPENAI_API_KEY=your-api-key`
- **Usage**:
  - Run the script in your terminal with `python api_model.py`.
  - The script interacts with the OpenAI API, generating content that is saved as `sju_sustainability_plan_draft.txt` in the working directory.

### Text Extraction Scripts
- `extract_txt.py` / `extract_word.py`
  - **Purpose**: Extract text from PDF documents within the `./Sustainability Plans` folder.
  - **Usage**: Execute the scripts to process and extract text from PDF files located in the specified folder.

### `summarize.py`
- **Purpose**: Creates summaries of existing sustainability plans, aiding in content generation.
- **Usage**: Analyzes and summarizes text files containing sustainability plans.

### `gpt.py`
- **Purpose**: Offers a command-line interface for interactive querying with GPT.
- **Usage**: Run the script for real-time interaction and testing with the GPT model.

### `pdf.py`
- **Purpose**: Converts and formats the generated text into a PDF document.
- **Usage**: Post content generation, execute the script to obtain a formatted PDF version of the plan.

### Experimental Scripts
- `fine_tuned_model.py` and `extract_train_validation.py`
  - **Purpose**: Initially used for experimenting with model fine-tuning and data preparation.
  - **Usage**: Not employed in the final version of the project; for experimental reference only.

## Installation & Configuration
- Install Python 3.x and the required packages listed in `requirements.txt`.
- Set the OpenAI API key as an environment variable for scripts that interface with the OpenAI API.

