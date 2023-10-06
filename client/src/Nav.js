// src/Homepage.js

import React from 'react';
import {Link} from'react-router-dom';
import './Navbar.css';

function Navbar (){
return (
    <nav className="navbar">
        <ul className="nav-list">
            <li className="nav-item"><Link to="/">Home</Link></li>
            <li className="nav-item"><Link to="/properties">Properties</Link></li>
            <li className="nav-item"><Link to="/aboutus">About Us</Link></li>
            <li className="nav-item"><Link to="/contact">Contact</Link></li>
            <li className="nav-item"><Link to="/Login">Log in</Link></li>
        </ul>
    </nav>
)
}




export default Navbar;



