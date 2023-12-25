from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set your API key

# Write a function to send a prompt to GPT-4 and receive a response
def get_input(prompt, info, model="gpt-4-1106-preview", max_tokens=4096):
    response = client.chat.completions.create(model=model,
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": info}
    ],
    max_tokens=max_tokens)
    return response.choices[0].message.content

# Function to get multiline user input
def get_multiline_input(prompt_message):
    print(prompt_message)
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return '\n'.join(lines)

# A multiline prompt is inputted into get_input, and the output is printed
while True:
    # prompt = get_multiline_input("Enter GPT Prompt. Ctrl-D to save it.\n" + "-" * 50 + "\n")
    prompt = "You are a personal assistant."
    input_text = get_multiline_input("Enter GPT input. Hit enter and then Ctrl-D to save it.\n" + "-" * 50 + "\n")

    print("Generating Results...")
    model_result = get_input(prompt, input_text)

    # Print a line of dashes
    print("-" * 50)
    print(model_result)
    print("-" * 50, "\n")
