import React, { useState } from 'react';
import { askQuestion } from './api';

function MessageInput({ addAnswer, file }) {
  const [question, setQuestion] = useState('');
  const [isAnswering, setIsAnswering] = useState(false);

  const handleQuestionChange = (event) => {
    setQuestion(event.target.value);
  };

  const handleAskQuestion = async () => {
    if (!file) {
      alert('Please upload a PDF file first.'); // Check if a PDF has been uploaded
      return;
    }


    setIsAnswering(true)
    try {
      if (question.trim()) {
        const newAnswer = await askQuestion(question);
        addAnswer(newAnswer);
        setQuestion('');
        setIsAnswering(false);
      }
    } catch (error) {
      alert('Error Answering');
      setIsAnswering(false);
    }


  };

  return (
    <div className="input-area">
      <input
        className="input-box"
        type="text"
        value={question}
        onChange={handleQuestionChange}
        placeholder="Ask a question..."
        onKeyDown={event => event.key === 'Enter' ? handleAskQuestion() : null}
      />

      <button className="send-button" onClick={handleAskQuestion} disabled={isAnswering || !question}>
        {isAnswering ? 'Thinking...' : 'Send'}
      </button>
    </div>
  );
}

export default MessageInput;