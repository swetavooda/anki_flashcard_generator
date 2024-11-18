from flask import Flask, jsonify, request, redirect, url_for, send_file,render_template
import os

from flashcard_generator import generate
# from utils.your_script import process_pdf  # Adjust this import if needed

app = Flask(__name__)

# Adjust paths to point to the correct folders
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # One level above
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'frontend/uploads')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'frontend/output')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


@app.route('/')
def upload_file():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def handle_file():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400

    # Save uploaded file
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    file.save(pdf_path)

    # Process the file with your script
    output_csv = os.path.join(app.config['OUTPUT_FOLDER'], f"{os.path.splitext(file.filename)[0]}.csv")
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    process_pdf(pdf_path, output_csv)  # Ensure this function works with full paths
# Generate the download URL
    download_url = url_for('download_file', filename=os.path.basename(output_csv))
    return jsonify({"success": True, "download_url": download_url})

@app.route('/download/<filename>')
def download_file(filename):
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    return send_file(output_path, as_attachment=True)

def process_pdf(input_path, output_path):
    print('in porcess_pdf',input_path,output_path)
    generate(input_path,output_path)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    app.run(debug=True)
