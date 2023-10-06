import React, { useState } from 'react';
import './Loginform.css'; // Create a CSS file for styling
import { useNavigate } from 'react-router-dom';

function Loginform() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);
  const [errors, setErrors] = useState([]);
  const navigate = useNavigate();
  const [agentId, setAgentId] = useState(null); 

  function onAddAgent() {
    console.log('Agent added successfully!');
  }

  function handleLogin() {
    const formData = {
      username: username,
      password: password,
    };

    fetch('http://127.0.0.1:5555/agentlogin', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((r) => {
        if (r.ok) {
          
          r.json().then((data) => {
            const { agent_id } = data; 
            setAgentId(agent_id); 
            onAddAgent();
            navigate(`/redirect?username=${username}&password=${password}&agent_id=${agent_id}`);
          });
        } else {
          r.json().then((err) => setErrors(err.errors));
        }
      });
  }

  function handleRegister() {
    const formData = {
      username: username,
      password: password,
    };

    fetch('http://127.0.0.1:5555/agents', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((r) => {
        console.log(formData);
        console.log(r);

        if (r.ok) {
          onAddAgent();
          navigate('/redirect?username=' + username + '&password=' + password); 
        } else {
          r.json().then((err) => setErrors(err.errors));
        }
      });
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (isRegistering) {
      handleRegister();
    } else {
      handleLogin();
    }
  }

  return (
    <>
      <div className="background">
        <div className="shape"></div>
        <div className="shape"></div>
      </div>
      <form onSubmit={handleSubmit}>
        {isRegistering ? <h3>Register as an Agent</h3> : <h3>Agents Login Here</h3>}

        <label htmlFor="username">Username</label>
        <input
          type="text"
          placeholder="Username"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <label htmlFor="password">Password</label>
        <input
          type="password"
          placeholder="Password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">
          {isRegistering ? 'Register' : 'Log In'}
        </button>

        <button
          type="button"
          onClick={() => setIsRegistering(!isRegistering)}
          className="toggle-button"
        >
          {isRegistering ? 'Already have an account? Log in' : "Don't have an account? Register"}
        </button>
      </form>
    </>
  );
}

export default Loginform;
