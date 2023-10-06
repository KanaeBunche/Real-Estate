import React, { useState } from 'react';
import './Contactform.css';


function ContactForm() {
  const [userName, setUserName] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState(null);

  const handleSubmitContact = async (e) => {
    e.preventDefault();

    const formData = {
      username: userName,
      message: message,
    };

    try {
      const response = await fetch("http://127.0.0.1:5555/contacts-list", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        console.log("Success!");
        
        setUserName("");
        setMessage("");
        setError(null);
      } else {
        const errorData = await response.json();
        setError(errorData.error);
      }
    } catch (error) {
      console.error("Error:", error);
      setError("An error occurred while submitting the form.");
    }
  };

  return (
    <div>
      <div className="background">
        <div className="shape"></div>
        <div className="shape"></div>
      </div>
      <form className="conform" onSubmit={handleSubmitContact}>
        <h3>Leave Any Feedback</h3>
        <div className="form-content">
          <div className="left">
            <label htmlFor="UserName">User Name</label>
            <input
              type="text"
              placeholder="User Name"
              id="UserName"
              value={userName}
              onChange={(e) => setUserName(e.target.value)}
              required
            />
          </div>
          <div className="right">
            <label htmlFor="message">Message</label>
            <textarea
              id="message"
              placeholder="Your message..."
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              required
            ></textarea>
          </div>
        </div>

        {error && <div className="error">{error}</div>}

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default ContactForm;
