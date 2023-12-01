import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import db  from './Database'

function Signup() {
    const navigate = useNavigate();
    const [id, setId] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    
    const handleSubmit = (event) => {
        event.preventDefault();
        // Handle the signup logic here
        db(id, phoneNumber);
        console.log('ID:', id, 'Phone Number:', phoneNumber);
        // You might want to send this data to a server or use it in some other way
    };

    const handleNavigate = () => {
        navigate('/socket-counter');
    };

    return (
        <div className="signup-page">
            <form onSubmit={handleSubmit}>
                <div>
                    <input type="text"  value={id} placeholder="GTID" onChange={(e) => setId(e.target.value)}/>
                </div>
                <br />
                <div>
                    <input type="tel" value={phoneNumber} placeholder="Phone Number" onChange={(e) => setPhoneNumber(e.target.value)}/>
                </div>
                <br />
                <button type="submit" onClick={handleSubmit}>Sign In</button>
            </form>
            <button type="button" onClick={handleNavigate}>Skip</button>
        </div>
    );
}

export default Signup;
