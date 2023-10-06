import React,{useState} from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Home";
import Properties from "./Properties";
import About from "./About";
import Contact from "./Contact";
import Login from "./Login";
import RedirectedPage from "./Redirectpage";
import Button from 'react-bootstrap/Button';
import { Chatbox, ChatboxProvider } from './Chatbox';
import Navbar from "./Nav";
import './Chatbox.css'



const App = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);

  const toggleChat = () => {
    setIsChatOpen(!isChatOpen);
  };
  return (
    <div>
      
    <BrowserRouter>
    <Button  variant="light" className="chat-button" onClick={toggleChat}>
        Chat
      </Button>
      <ChatboxProvider>
        <Chatbox isOpen={isChatOpen} toggleChat={toggleChat} />
      </ChatboxProvider>

      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/properties" element={<Properties />} />
        <Route path="/aboutus" element={<About/>} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/login" element={<Login />} />
        <Route path="/redirect" element={<RedirectedPage />} />
      </Routes>
      <Navbar />
    </BrowserRouter>
    </div>
  );
};

export default App;
