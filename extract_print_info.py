import openai  # Import the OpenAI library for API access

#Open and read the resume file, returning it's content as a string
def read_resume(file_path): 
    with open(file_path, 'r') as file:
        return file.read()
    
#Store and return all the extracted information 
def extract_information(resume_text, api_key):
    # Set the OpenAI API key for authentication
    openai.api_key = api_key

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

    # Sending the resume text to OpenAI's API and asking it to extract structured information from prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the model to the most capable and latest model
        prompt=prompt_text,  # The prompt to the model, including the resume text
        max_tokens=2000,  # Limit the number of tokens (words and characters) the model can generate
        temperature=0.5,  # Control the randomness of the output, 0.5 helps balance between coherence and creativity
        top_p=1.0,  # Nucleus sampling: 1.0 means no sampling, the model uses full range of probabilities
        frequency_penalty=0.0,  # Penalizes new tokens based on their frequency in the text so far
        presence_penalty=0.0  # Penalizes new tokens based on whether they have appeared in the text so far
    )

    # Extract and return the response text
    return response.choices[0].text.strip()