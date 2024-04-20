import React, { useState } from 'react';
import '../css/Chat.css'; // Check path based on your project structure
import ChatHeader from './ChatHeader';
import MessageList from './MessageList';
import MessageInput from './MessageInput';

function Chat() {
  const [file, setFile] = useState();
  const [answers, setAnswers] = useState([]);

  const addAnswer = (newAnswer) => {
    setAnswers([...answers, newAnswer]);
  };

  const clearAnswers = () => {
    setAnswers([]);
  };

  return (
    <div className="chat-container">
      <ChatHeader addAnswer={addAnswer} file={file} setFile={setFile} />
      <MessageList answers={answers} clearAnswers={clearAnswers} />
      <MessageInput addAnswer={addAnswer} file={file} />
    </div>
  );
}

export default Chat;
