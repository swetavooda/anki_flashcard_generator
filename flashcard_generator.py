import os
import openai
import csv
from PyPDF2 import PdfReader

# Set your OpenAI API key here if not set as env variable
# os.environ["OPENAI_API_KEY"] = ""
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to parse PDF content
def parse_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    raw_text = ''
    for page in reader.pages:
        content = page.extract_text()
        if content:
            raw_text += content
    return raw_text

# Function to use OpenAI API to generate flashcards in CSV-compatible format
def ask_openai_generate_csv(text_chunk, difficulty, reverse = False, model="gpt-4o-mini"):
    """
    Generate flashcards in CSV-compatible format for ANki
    """
    if reverse:
        system_message = f"""
        You are a professional Anki flashcard creator. Your task is to create a list of reversible flashcards in CSV format.

        ### Guidelines:
        1. Each flashcard should have 4 fields: Question, Answer, Tags.
        2. Ensure that the cards are reversible, meaning both the Question and Answer must be clear and make sense when flipped.
        3. Use concise, focused language to avoid lengthy sentences or unnecessary details. Both the Question and Answer should fit comfortably on a standard flashcard.
        4. Avoid including chapter names or long explanations in the Question or Answer fields. Focus on specific concepts or facts.
        3. Avoid phrases like "What is..." or "Explain...". Instead, use specific terms or short phrases.
        5. Use the following CSV format with a pipe (|) delimiter:
           Question|Answer|Tags
        6. Examples of good reversible flashcards:
           Inertia|Resistance to motion change|inertia, physics, motion
           Newton's 2nd Law|F=ma|Newton's Laws

        ### Input Text:
        {text_chunk}

        ### Instructions:
        Generate reversible flashcards from the text above based on the difficulty level ({difficulty.capitalize()}). Ensure proper CSV formatting with a pipe delimiter. Avoid including chapter names or overly broad topics.
        """
    else:
        system_message = f"""
        You are a professional Anki flashcard creator. Your task is to create a list of flashcards in CSV format.

        ### Guidelines:
        1. Each flashcard should have 4 fields: Question, Answer, Tags.
        2. Use concise, specific language to create questions and answers that focus on key facts or concepts. Avoid lengthy explanations.
        3. Avoid referencing chapter names or general overviews in the Question or Answer fields.
        3. Avoid phrases like "What is..." or "Explain...". Instead, use specific terms or short phrases.
        4. Use the following CSV format with a pipe (|) delimiter:
           Question|Answer|Tags
        5. Examples of concise, focused flashcards:
           Density|Mass/volume|density, physics, formula
           Define potential energy|Stored energy|energy, physics, potential

        ### Input Text:
        {text_chunk}

        ### Instructions:
        Generate flashcards from the text above based on the difficulty level ({difficulty.capitalize()}). Ensure proper CSV formatting with a pipe delimiter. Avoid including chapter names or unnecessary details in the flashcards.
        """

    # Send the system and user message to the OpenAI API
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
        ],
        max_tokens=800,
        temperature=0.3
    )

    return response['choices'][0]['message']['content'].strip()

# Function to process OpenAI output and save it to a CSV
def process_and_save_csv(ai_output, output_file):
    try:
        # Split the output into lines
        lines = ai_output.splitlines()
        
        # Validate and sanitize each line
        cleaned_data = []
        for line in lines:
            # Ensure the line has exactly 3 fields (Question|Answer|Tags)
            if line.count("|") == 2:
                fields = [field.strip() for field in line.split("|")]
                # Escape quotes and problematic characters
                fields = [field.replace('"', '""') for field in fields]
                cleaned_data.append(fields)

        # Save to CSV
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(cleaned_data)
        print(f"Flashcards saved to {output_file}")
    except Exception as e:
        print(f"Error processing AI output: {e}")

