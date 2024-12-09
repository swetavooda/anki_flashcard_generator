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
5. **Run the Application**:
   ```bash
   flask run
   ```
   This will start the Flask app, accessible at `http://127.0.0.1:5000/`.