import React from 'react';
import { Link } from 'react-router-dom';
import './Card.css';

const Card = ({ title, image, description, link }) => {
    return (
        <div className="card">
            <img src={image} alt={title} className="card-image" />
            <div className="card-content">
                <h3 className="card-title">{title}</h3>
                <p className="card-description">{description}</p>
                <Link to={link} className="card-button">Se oppskrift</Link>
            </div>
        </div>
    );
};

export default Card;