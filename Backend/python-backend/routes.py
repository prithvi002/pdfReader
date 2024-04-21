from flask import Blueprint, jsonify, request
import os
import shutil
from config import Config
from pdf_processing import extract_and_create_context, create_chain
from langchain_core.messages import HumanMessage, AIMessage

main = Blueprint('main', __name__)

context = None
chat_history = []

@main.route('/')
def home():
    return jsonify({'message': 'Welcome to the PDF Reader!'})

@main.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    
    global context
    global chat_history
    
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

    context = extract_and_create_context(folder_path)
    chat_history = []
    return jsonify({'success': 'File uploaded successfully'})

@main.route('/ask-question', methods=['POST'])
def ask_question():
    
    global context
    global chat_history
    
    chain = create_chain(context)
    question = request.json.get('question')
    response = chain.invoke({
    "input": question,
    "chat_history":chat_history})
    
    chat_history.append(HumanMessage(content=question))
    chat_history.append(AIMessage(content=response['answer']))
    
    return jsonify(answer=response['answer'])