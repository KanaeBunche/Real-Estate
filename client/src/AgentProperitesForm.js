import React, { useState } from 'react';
import './AgentPropForm.css';
import { useLocation} from 'react-router-dom';


function AgentPropertiesForm() {

  const [title, setTitle] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  
  
  const [showSuccessMessage, setShowSuccessMessage] = useState(false);
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const agentId = queryParams.get('agent_id');


  const handleSubmit = async (e) => {
    e.preventDefault();
  

    const formData = {
      title,
      image_url: imageUrl,
      description,
      price,
    };
  
    try {
      
      const propertyResponse = await fetch('http://127.0.0.1:5555/properties', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
  
      if (propertyResponse.ok) {
        console.log('Property successfully added');
        setShowSuccessMessage(true); 
  
        
        setTitle('');
        setImageUrl('');
        setDescription('');
        setPrice('');
  
        
        const propertyData = await propertyResponse.json(); 
  

        const associationData = {
          agent_id: agentId, 
          property_id: propertyData.id,
        };
        console.log(associationData);
  
      
        const associationResponse = await fetch('http://127.0.0.1:5555/agent-properties', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(associationData),
        });
  
        if (associationResponse.ok) {
          console.log('Property successfully associated with the agent');
        } else {
          console.error('Error associating property with the agent');
        }
  
        
        setTimeout(() => {
          setShowSuccessMessage(false);
        }, 10000);
      } else {
        console.error('Error adding property');
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }
  };
  

  return (
    <div>
      
      <form className="agentform" onSubmit={handleSubmit}>
        <h3>Agents Property</h3>
        <div>
          
          {showSuccessMessage && (
            <div className="success-message">
              Your property was added!
            </div>
          )}

          <div>
            <label htmlFor="title">Title</label>
            <input
              type="text"
              placeholder="Title"
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            />

            <label htmlFor="image_url">Image URL</label>
            <input
              type="text"
              placeholder="Image URL"
              id="image_url"
              value={imageUrl}
              onChange={(e) => setImageUrl(e.target.value)}
              required
            />

            <label htmlFor="description">Description</label>
            <input
              type="text"
              placeholder="Description"
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              required
            />

            <label htmlFor="price">Price</label>
            <input
              type="text"
              placeholder="Price"
              id="price"
              value={price}
              onChange={(e) => setPrice(e.target.value)}
              required
            />
          </div>
        </div>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default AgentPropertiesForm;
