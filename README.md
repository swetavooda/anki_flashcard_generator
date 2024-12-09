### README: AI-Powered Flashcard Generator

---

#### **Overview**
The **AI-Powered Flashcard Generator** automates the creation of flashcards compatible with Anki, a popular spaced-repetition flashcard app. Users can upload text-based PDFs, customize difficulty levels, and generate reversible flashcards. The tool leverages AI to produce concise, well-structured flashcards tailored to diverse learning preferences.

---

#### **Features**
1. **Anki Integration**: Generates flashcards in CSV format compatible with Anki’s import functionality.
2. **Reversible Cards**: Supports bidirectional learning with reversible flashcards.
3. **Difficulty Levels**: Allows selection of Easy, Medium, or Hard flashcards.
4. **Dynamic Tagging**: Automatically assigns meaningful tags for better organization.
5. **PDF Parsing**: Efficiently processes text-based PDFs using PyPDF2.
6. **User-Friendly Interface**: Built using Flask for seamless file uploads and customization.

---

#### **Requirements**
- Python 3.8+
- Virtual Environment (optional but recommended)
- Dependencies listed in `requirements.txt`

---

#### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-repo>/flashcard-generator.git
   cd flashcard-generator
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Environment Variables**:
   Set your OpenAI API key in the `.env` file:
   ```env
   OPENAI_API_KEY=<your-openai-api-key>
   ```

---

#### **Usage**
1. **Run the Application**:
   ```bash
   flask run
   ```
   This will start the Flask app, accessible at `http://127.0.0.1:5000/`.

2. **Upload a PDF**:
   - Visit the homepage.
   - Upload a text-based PDF file.
   - Choose the difficulty level (Easy, Medium, Hard).
   - Select the flashcard type (Regular or Reversible).

3. **Download Flashcards**:
   - After processing, download the generated CSV file.
   - Import the CSV file into Anki:
     - Open Anki and go to `File > Import`.
     - Select the downloaded CSV file and configure import settings.

---

#### **Customization**
- **Difficulty Levels**:
  Adjust the complexity of flashcards to suit beginner, intermediate, or advanced learners.
- **Reversible Cards**:
  Enable or disable reversible cards based on learning preferences.

---

#### **Development Setup**
1. **[IMPORTANT] Environment Variables**:
   Set your OpenAI API key in the `.env` file:
   ```env
   OPENAI_API_KEY=<your-openai-api-key>
   ```

2. **Folder Structure**:
   ```
   flashcard-generator/code
   ├── app.py             # Main Flask app
   ├── templates/         # HTML templates for the web interface
   ├── static/            # CSS and JavaScript files
   ├── uploads/           # Uploaded PDF files
   ├── output/            # Generated CSV files
   └── requirements.txt   # Dependencies
   ```

---

#### **Limitations**
- Supports only text-based PDFs (no images, videos, or scanned PDFs).
- Limited support for processing mathematical formulas.
- Customization is limited to predefined options.

---

#### **Future Improvements**
- Add support for multimedia formats (images, videos).
- Enhance mathematical formula parsing and rendering.
- Introduce multi-language support for flashcard generation.

---

#### **Contributing**
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Create a pull request on the main repository.

---

#### **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

#### **Contact**
For questions or feedback, contact **Sweta Vooda** at svooda3@gatech.edu.