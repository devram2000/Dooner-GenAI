import os 
import openai


def generate_sustainability_plan(model_name, organization):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are an AI trained to create sustainability plans for universities."},
                {"role": "user", "content": f"Create a sustainability plan for {organization}."}
            ]
        )

        plan = response.choices[0].message if response.choices else "No response generated."
        return plan
    except Exception as e:
        return str(e)

# Usage
model_name = "ft:gpt-3.5-turbo-1106:personal::8Nm2Lda3"  # Name of your fine-tuned model
organization = "Saint Joseph's University"
plan = generate_sustainability_plan(model_name, organization)
print(plan)
