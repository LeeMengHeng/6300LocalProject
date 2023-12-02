import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Signup.css';

function Signup() {
    const navigate = useNavigate();
    const [id, setId] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    
    const handleSubmit = (event) => {
        event.preventDefault();
        // Handle the signup logic here
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
                    <input class="input-id" type="text"  value={id} placeholder="GTID" onChange={(e) => setId(e.target.value)}/>
                </div>
                <br />
                <div>
                    <input class="input-phone" type="tel" value={phoneNumber} placeholder="Phone Number" onChange={(e) => setPhoneNumber(e.target.value)}/>
                </div>
                <br />
                <button class="submit" type="submit" onClick={handleSubmit}>Sign In</button>
            </form>
            <button type="button" onClick={handleNavigate}>Skip</button>
        </div>
    );
}

export default Signup;
