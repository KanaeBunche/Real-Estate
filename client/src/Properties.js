import React, { useEffect, useState } from "react";
import Nav from "./Nav";
import EditProperty from "./Edit";

import "./Properties.css";

function Properties() {
  const [propertyData, setPropertyData] = useState([]);
  const filteredPropertyData = propertyData.slice(6);
  

  const handleDeleteProperty = (propertyId) => {
    
    fetch(`http://127.0.0.1:5555/properties/${propertyId}/delete`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => {
        if (response.ok) {
          
          const updatedPropertyData = propertyData.filter(property => property.id !== propertyId);
          setPropertyData(updatedPropertyData);
        } else {
          
          console.error('Failed to delete property.');
        }
      })
      .catch(error => {
        console.error('Error occurred while deleting property:', error);
      });
  };


  

  useEffect(() => {
    // Fetch data from your backend API
    fetch("http://127.0.0.1:5555/properties-list")
      .then((response) => response.json())
      .then((propertyData) => {
        console.log(propertyData);
        // Set the propertyData state variable
        setPropertyData(propertyData);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  

  return (
    <>
      <Nav />
    
      <div className="bodie">
      <h1 className="proplist"> Local Property Listings</h1>
        <div className="App">
        {filteredPropertyData.map((property) => (
            <div key={property.id} className="HorizontalCard">
              
              <div className="PropertyCard__image">
            <img src={property.image_url} alt={property.title} />
                <div className="image-placeholder"></div>
              </div>
              <div className="PropertyCard__info">
  <p className="PropertyCard__title">{property.title}</p>
  <p className="PropertyCard__price">Price: {`$${property.price}`}</p>
  <div style={{ display: "flex", alignItems: "center" }}>
    <p className="PropertyCard__description">{property.description}</p>
    <button className="delete" onClick={() => handleDeleteProperty(property.id)}>
      x
    </button>
    
  </div>
  <EditProperty property={property} />
</div>

            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default Properties;
