# Resume Information Extractor

This project extracts specific information from a plain text resume using OpenAI's GPT-3.5-turbo model. The extracted information includes:

- First name
- Last name
- Phone number
- Email address
- List of employers
- Start and end dates for each employer
- Job titles for each job
- Job details/work descriptions
- Education details

## Files

- `extract_info.py`: Contains functions to read the resume and extract information using OpenAI's API.
- `main.py`: The main script that loads the resume, extracts information, and prints it.
- `resume.txt`: Sample resume file in plain text format.

## Setup

### Prerequisites

- Python 3.7+
- An OpenAI API key

### Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install openai
    ```

4. Set the OpenAI API key:
    ```sh
    export api_key='your_openai_api_key'
    ```

## Usage

1. Ensure the `resume.txt` file contains the resume in plain text format.
2. Run the main script with the resume file path as an argument:
    ```sh
    python main.py resume.txt
    ```

3. The script will print the extracted information on the screen.

## Example

```sh
$ python main.py resume.txt
Extracted Information:
First name: John
Last name: Doe
Phone number: (123) 456-7890
Email address: john.doe@example.com
Employers: 
  - Employer: ABC Corp
    Start Date: Jan 2020
    End Date: Dec 2021
    Job Title: Software Engineer
    Job Details: Developed and maintained web applications
  - Employer: XYZ Inc
    Start Date: Feb 2018
    End Date: Dec 2019
    Job Title: Junior Developer
    Job Details: Assisted in developing mobile applications
Education Details:
  - Bachelor of Science in Computer Science, University of Example, 2017
