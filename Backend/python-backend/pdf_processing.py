# pdf_processing.py
import os
import pdfplumber

def extract_text_from_pdf(folder_path):
    pdf_file = next((f for f in os.listdir(folder_path) if f.endswith('.pdf')), None)
    if pdf_file is None:
        return "No PDF file found."

    pdf_path = os.path.join(folder_path, pdf_file)
    output_txt_path = os.path.join(folder_path, 'extracted_text.txt')
    
    with pdfplumber.open(pdf_path) as pdf:
        text = []
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text.append(extracted_text)

    with open(output_txt_path, 'w', encoding='utf-8') as out_file:
        out_file.write('\n'.join(text))
    
    return f"Text successfully extracted to {output_txt_path}"
