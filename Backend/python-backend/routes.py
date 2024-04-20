# routes.py
from flask import Blueprint, jsonify, request
import os
import shutil
from config import Config
from pdf_processing import extract_text_from_pdf

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({'message': 'Welcome to the PDF Reader!'})

@main.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '' or not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Invalid file. Please upload a PDF file'})

    folder_path = Config.UPLOAD_FOLDER

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

    full_path = os.path.join(folder_path, file.filename)
    file.save(full_path)

    extract_text_from_pdf(folder_path)
    return jsonify({'success': 'File uploaded successfully'})

@main.route('/ask-question', methods=['POST'])
def ask_question():
    question = request.json.get('question')
    print('Received question:', question)
    return jsonify(answer="Question received successfully")
