import openai
from openai import OpenAI
import os 

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set your API key

# Function to send a prompt to GPT-4 and receive a response
def get_input(prompt, info, model="gpt-4-1106-preview", max_tokens=4096):
    try:
        response = client.chat.completions.create(model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": info}
        ],
        max_tokens=max_tokens)
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None

# Embedded document contents (replace these placeholders with actual contents of your documents)
prompt = '''
Analyze the following dataset of academic job postings, which is structured as a list of lists. 
Each sublist contains information about a specific university's center or institute, 
including the school name, the center or institute name, a descriptive blurb, and listed 
responsibilities for the director role. Based on this analysis, provide a summary of common responsibilities, 
qualifications, and thematic elements that are essential for a director's position at a university's center or institute. 
Then, use these insights to create a template for a job posting for a director position at Saint Joseph's University (SJU). 
The template should be tailored to appeal to candidates in a non-technical manner, highlighting key responsibilities, 
required qualifications, and the ethos of a typical academic center or institute. The format of the input is: 
[[school 1 name, school 1 center/institute that is looking for a director, school 1 text blurb about the center or institute, school 1 responsibilities], ..., [...]].
Note that for the responsibilities, the input is in bullet form, but the bullets didn't read. Make sure to recognize that if there is a period and then
another word after it or two words combined together, a bullet should be there. In the output, give a sample of responsibilities that can be used after giving all of the insights.
'''

with open('school_responsibilities.txt') as f:
    combined_input = ''.join(f.readlines())

# Generate the sustainability plan
print("Generating the Responsibilities for SJU...")
model_result = get_input(prompt, combined_input)

# Define the filename for the output
output_filename = 'sju_job_responsibilities_draft.txt'

# Save the generated plan to a file
with open(output_filename, 'w') as file:
    file.write("-" * 50 + "\n")
    file.write(model_result)
    file.write("\n" + "-" * 50)

print(f"Responsibilities have been saved to {output_filename}")
