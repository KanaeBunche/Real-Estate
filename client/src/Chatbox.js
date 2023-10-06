import React, { useState, useContext } from 'react';
import './Chatbox.css';

const ChatboxContext = React.createContext({
  messages: [],
  setMessages: () => {},
});

const ChatboxProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);

  return (
    <ChatboxContext.Provider value={{ messages, setMessages }}>
      {children}
    </ChatboxContext.Provider>
  );
};

const ChatboxMessage = ({ message, author }) => {
  return (
    <div>
      <strong>{author}</strong>: {message}
    </div>
  );
};

const Chatbox = ({ isOpen, toggleChat }) => {
  const { messages, setMessages } = useContext(ChatboxContext);

  const questions = [
    "Is this website easy to use? (yes or no)",
    "Would you recommend this website to anyone? (yes or no)",
    "Are you a real estate agent? (yes or no)",
  ];

  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answered, setAnswered] = useState(false);
  const [showForm, setShowForm] = useState(true); // Manage form visibility

  const handleResponse = (response) => {
    if (!answered) {
      setMessages([...messages, { message: questions[currentQuestion], author: 'Bot' }]);
      setMessages([...messages, { message: response, author: 'User' }]);
  
      if (currentQuestion < questions.length - 1) {
        setCurrentQuestion(currentQuestion + 1);
      } else {
        setAnswered(true); // Set answered to true to prevent further interaction
        setShowForm(false); // Hide the form
      }
    }
  };
  

  const handleRestart = () => {
    setMessages([]); // Clear chat history
    setCurrentQuestion(0);
    setAnswered(false); // Allow answering questions again
    setShowForm(true); // Show the form again
  };
  

  return (
    <div className={`chatbox ${isOpen ? 'open' : ''}`}>
      <h1>Chatbox</h1>
      <ul className='font'>
        {messages.map((message, index) => (
          <ChatboxMessage  key={index} message={message.message} author={message.author} />
        ))}
      </ul>
      {showForm && currentQuestion < questions.length ? (
        <div className='font'>
          <p className='font'>{questions[currentQuestion]}</p>
          <button
            onClick={() => handleResponse('Yes')}
            disabled={answered}
            style={{ fontSize: '12px', padding: '5px 10px' }}
          >
            Yes
          </button>
          <button className='font'
            onClick={() => handleResponse('No')}
            disabled={answered}
            style={{ fontSize: '12px', padding: '5px 10px' }}
          >
            No
          </button>
        </div>
      ) : null}
      {answered && (
        <div>
          <p className='font'>Questions answered. Click below to restart.</p>
          <button onClick={handleRestart}>Restart</button>
        </div>
      )}
    </div>
  );
};

export { Chatbox, ChatboxProvider };
