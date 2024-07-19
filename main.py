import sys
from extract_info import read_resume, extract_information  # Import the required functions

def main():
    # Check if the command line argument for the resume file path is provided
    if len(sys.argv) < 2:
        print("Please add your resume: <resume_file_path>")
        sys.exit(1)  # Exit the script if no argument is provided
    
    resume_file_path = sys.argv[1]  # Get the resume file path from command line arguments
    
    # Load the resume text from the provided file path
    resume_text = read_resume(resume_file_path)
    
    # Extract the detailed information using OpenAI
    extracted_info = extract_information(resume_text)
    
    # Print the structured information extracted from the resume
    print("Extracted Information:")
    print(extracted_info)

if __name__ == "__main__":
    main()
