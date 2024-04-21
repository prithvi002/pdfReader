import React, { useState } from 'react';
import { uploadPdf } from './api';

function ChatHeader({ addAnswer, file, setFile }) {
  const [isUploading, setIsUploading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    console.log("PDF file uploaded:", event.target.files[0].name);
  };

  const handleSendPdf = async () => {
    if (!file) {
      alert('Please upload a PDF file first.');
      return;
    }

    setIsUploading(true);
    try {
      await uploadPdf(file);
      setIsUploading(false);
    } catch (error) {
      alert('Error uploading PDF');
      setIsUploading(false);
    }
  };

  return (
    <header className="chat-header">
      <h1>Chat Application</h1>
      <div className="file-upload">
        <div className="file-input">
          <input type="file" onChange={handleFileChange} disabled={isUploading} accept="application/pdf" />
        </div>
        <button className="upload-pdf-button" onClick={handleSendPdf} disabled={isUploading}>
          {isUploading ? 'Uploading...' : 'Upload'}
        </button>
      </div>
    </header>
  );
}

export default ChatHeader;