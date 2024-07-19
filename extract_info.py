from openai import OpenAI  # Ensure correct import of the OpenAI library
import os


def read_resume(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extract_information(resume_text):
    # Set the OpenAI API key for authentication
    client = OpenAI( api_key=os.environ.get("api_key"))

    # Define a detailed prompt for the AI to follow, explicitly requesting structured information
    prompt_text = f"""
    Extract detailed information from the following resume:
    {resume_text}
    Please provide the following details in a structured format:
    - First name of the person
    - Last name of the person
    - Phone number of the person
    - Email address of the person
    - List of employers that the person has worked with
    - Start date and end date for each of the employer
    - Job title for each of the job with each of the employer
    - Job details/work for each of the job
    - Education details of the person
    """

    # Sending the resume text to OpenAI's API and asking it to extract structured information
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Ensure the model version is correct
        messages=[
            {"role": "system", "content": "You are a helpful assistant, skilled in professional resume analysis."},
            {"role": "user", "content": prompt_text}
        ]
    )

    # Extract and return the response text
    return response.choices[0].message  # Updated access method according to the API
