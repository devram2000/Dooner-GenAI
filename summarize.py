import openai
import os
from tqdm import tqdm

# Function to split the corpus into individual university plans
def split_corpus_by_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        plans = content.split("Title:")[1:]
        plans = ["Title:" + plan.strip() for plan in plans]
    return plans

# Function to send a prompt to GPT-4 and receive a response
def get_input(prompt, info, model="gpt-4-1106-preview", max_tokens=4096):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": info}
        ],
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content

# Function to create an enhanced summary prompt for each university plan
def create_summary_prompt(plan):
    return f"""
    Analyze and summarize the following university sustainability plan, focusing on identifying unique and effective strategies, practices, and goals. Highlight elements that could be particularly beneficial or innovative for Saint John's University (SJU) as it develops its own sustainability plan. Consider aspects that could serve as a contrast to or an enhancement of SJU's existing initiatives, aligning with SJU's Jesuit values and commitment to environmental responsibility, social justice, and economic viability. Provide a concise yet comprehensive summary that SJU can use for comparison and potential integration:

    {plan}
    """
# Function to truncate text to a specific token limit
def truncate_to_token_limit(text, token_limit=100000):
    tokens = text.split()
    if len(tokens) > token_limit:
        return ' '.join(tokens[:token_limit])
    return text

# Function to create a combined summary from individual files
def create_combined_summary(output_dir, token_limit=100000):
    combined_summary = ""
    for filename in os.listdir(output_dir):
        if filename.endswith('_summary.txt'):
            with open(os.path.join(output_dir, filename), 'r', encoding='utf-8') as file:
                combined_summary += file.read() + "\n\n"

    return truncate_to_token_limit(combined_summary, token_limit)

# Function to create a safe filename using a counter
def create_safe_filename(counter):
    return f"university_plan_{counter}_summary.txt"

# Main script
def main(file_path, output_dir, max_filename_length=255):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    university_plans = split_corpus_by_title(file_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    counter = 1
    for plan in tqdm(university_plans):
        university_name = plan.split('\n')[0][6:].strip()  # Extracting the university name
        summary_filename = f"{university_name}_summary.txt"

        if len(summary_filename) > max_filename_length:
            summary_filename = create_safe_filename(counter)

        summary_file_path = os.path.join(output_dir, summary_filename)

        # Process and save summary if it doesn't already exist
        if not os.path.exists(summary_file_path):
            prompt = create_summary_prompt(plan)
            summary = get_input(prompt, plan)
            with open(summary_file_path, "w", encoding='utf-8') as summary_file:
                summary_file.write(summary)

        counter += 1

    # Create combined summary from all individual summaries
    combined_summary = create_combined_summary(output_dir)
    with open(os.path.join(output_dir, 'combined_summaries.txt'), 'w', encoding='utf-8') as combined_file:
        combined_file.write(combined_summary)

# Example usage
input_file_path = 'corpus.txt'  # Replace with the path to your .txt file
output_dir_path = 'university_summaries'  # Output directory
main(input_file_path, output_dir_path)
