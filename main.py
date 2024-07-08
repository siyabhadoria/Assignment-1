from extract_print_info import read_resume, extract_information  # Import the required functions

def main():
    # Load the resume text from a file
    resume_text = read_resume('resume.txt')
    # Your OpenAI API key, securely manage this key
    api_key = 'your_openai_api_key_here'
    # Extract the detailed information using OpenAI
    extracted_info = extract_information(resume_text, api_key)
    
    # Print the structured information extracted from the resume
    print("Extracted Information:")
    print(extracted_info)





    
