import React, { useState } from 'react';
import './Edit.css'

function EditProperty({ property }) {
  const [editedProperty, setEditedProperty] = useState(property);
  const [showForm, setShowForm] = useState(false);

  const handleEditButtonClick = () => {
    if (showForm) {
      setShowForm(false);
    } else {
      setShowForm(true);
    }
  };


  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setEditedProperty({
      ...editedProperty,
      [name]: value,
    });
  };

  const handleUpdateProperty = () => {
    fetch(`http://127.0.0.1:5555/putproperties/${property.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(editedProperty),
    })
      .then(response => {
        if (response.ok) {
          
          console.log('Property updated successfully.');
        } else {
          
          console.error('Failed to update property.');
        }
      })
      .catch(error => {
        console.error('Error occurred while updating property:', error);
      });
  };

  return (
    <div className='edithouse'>
      <button className='edit' onClick={handleEditButtonClick}> Edit </button>
      {showForm && (
        <div>
          <label>
            Title:
            <input
              type="text"
              name="title"
              value={editedProperty.title}
              onChange={handleInputChange}
              style={{ display: "block" }}
            />
          </label>
          <label>
            Price:
            <input
              type="number"
              name="price"
              value={editedProperty.price}
              onChange={handleInputChange}
              style={{ display: "block" }}
            />
          </label>
          <label>
            Description:
            <textarea className='text'
              name="description"
              value={editedProperty.description}
              onChange={handleInputChange}
              style={{ display: "block" }}
            />
          </label>
          <button onClick={handleUpdateProperty}>Update Property</button>
         
        </div>
      )}
    </div>
  );
}  

export default EditProperty;
