import os
import openai
from PyPDF2 import PdfReader
import csv

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "your_key"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to parse PDF content using PyPDF2
def parse_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    raw_text = ''
    for page in reader.pages:
        content = page.extract_text()
        if content:
            raw_text += content
    return raw_text

# Function to use OpenAI API to generate a list of questions and answers
def ask_openai(text_chunk, model="gpt-3.5-turbo"):
    # Define the system message to clearly instruct the model
    system_message = """
    You are a professional Anki flashcard creator. Your job is to create a list of concise questions and short, factual answers based on the provided text.
    
    Guidelines:
    - Each question should be specific, simple, and unambiguous.
    - The answer should be short (no more than 3 words), concise, and focused on key facts or concepts.
    - Use simple and easy-to-understand language.
    - Output the questions and answers as a list, one per line, formatted as:
      - "Question: [your question]"
      - "Answer: [your answer]"
    
    Here are some examples:
    ---
    Example 1:
    Text: The heart pumps blood through the circulatory system, delivering oxygen to cells.
    Question: What does the heart do?
    Answer: Pumps blood.
    ---
    Example 2:
    Text: The Pacific Ocean is the largest and deepest of Earth's oceanic divisions.
    Question: What is the largest ocean?
    Answer: Pacific Ocean.
    ---
    
    Now, using the following text, generate a list of questions and answers:
    """

    # Define the user message, passing the text chunk
    user_message = f"""
    Create a list of questions and answers from the following text:
    ---
    {text_chunk}
    ---
    Remember to keep the answers short (no more than 3 words) and focused on the key concepts from the text.
    """

    # Call the OpenAI API with the system and user messages
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        max_tokens=400,  # Increased max_tokens to handle a list of questions and answers
        temperature=0.3  # Lower temperature for more focused and deterministic responses
    )
    
    # Return the generated content
    return response['choices'][0]['message']['content'].strip()

# Function to generate flashcards
def generate_flashcards(text):
    flashcards = []
    
    # Split the text into smaller parts (optional, depending on size of content)
    text_chunks = [text[i:i + 1200] for i in range(0, len(text), 1200)]
    
    # Iterate over chunks to generate flashcards
    for chunk in text_chunks:
        # Ask OpenAI to generate a list of questions and answers
        flashcard_data = ask_openai(chunk)
        
        # Split the flashcard data into individual questions and answers
        lines = flashcard_data.splitlines()
        for i in range(0, len(lines), 2):  # Process pairs of lines as question and answer
            try:
                question = lines[i].replace("Question: ", "").strip()
                answer = lines[i + 1].replace("Answer: ", "").strip()
                flashcards.append((question, answer))
            except IndexError:
                # In case there's a mismatch in lines, skip this pair
                print(f"Skipping incomplete flashcard: {lines[i:i+2]}")
    
    return flashcards

# Function to export flashcards to a CSV file (compatible with Anki)
def export_flashcards_to_csv(flashcards, output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        #writer.writerow(['Question', 'Answer'])  # CSV header for Anki
        for question, answer in flashcards:
            writer.writerow([question, answer])
    print(f"Flashcards saved to {output_file}")

# Main function to run the workflow
def generate(pdf_path, output_file):
    # Step 1: Parse the PDF file
    parsed_text = parse_pdf(pdf_path)
    
    # Step 2: Generate flashcards using GPT-3.5-turbo
    flashcards = generate_flashcards(parsed_text)
    
    # Step 3: Export flashcards to CSV (Anki-compatible format)
    export_flashcards_to_csv(flashcards, output_file)
