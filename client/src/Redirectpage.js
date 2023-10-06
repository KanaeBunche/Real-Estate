
import React from 'react';
import AgentPropertiesForm from './AgentProperitesForm';
import './Redirect.css';

const RedirectedPage = () => {
  return (
    <div className='redirected-page'>
      <div className='welcome-container'>
        <h1 className='wh1'>Welcome! Thank you for signing in!</h1>
      </div>
      <AgentPropertiesForm />
    </div>
  );
};

export default RedirectedPage;

