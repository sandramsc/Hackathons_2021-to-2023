import React, { MouseEvent, useState } from 'react';
import { Link } from 'react-router-dom';
import { FaHeart, FaFacebook, FaLinkedin, FaGoogle } from 'react-icons/fa';
import logo from '../../assets/jpg/logo.jpg'

import './Login.css';

export default function Login() {
    const [showRegister, toggleRegister] = useState(false);

    let classnames = "container";

    if (showRegister) {
        classnames += " right-panel-active";
    }

    async function register(evt: MouseEvent) {
        evt.preventDefault();

        let data = {
            username : "Joe",
            email : "joe@gmail.com",
            password: "pass4567",
            jobTitle: "Amazing Software Engineer",
            department: "Cool Webshop"
        }

        const response = await fetch("http://localhost:4000/user/signup", 
        { method: "POST", headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data) });

        const payload = await response.json();

        console.log(payload);
    }
    <form>
        <h1>Sign Up</h1>
        <div className="social-container">
            <FaFacebook />
            <FaLinkedin />
            <FaGoogle />            
        </div>
        <span>or use your business email for registration</span>
        <input type="text" placeholder="Name" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        
        <input type="text" placeholder="Job Title" />
        <input type="text" placeholder="Start date" />
        <input type="text" placeholder="Team or Department" />
        
        <button type="button" onClick={register}>Sign Up</button>
    </form>

    return (
    <>
    <img src={logo} alt ="logo" className="logo"/>
    <div className={classnames} id="container">
        <div className="form-container sign-up-container">
            <form>
                <h1>Sign Up</h1>
                <div className="social-container">
                <FaFacebook />
                <FaLinkedin />
                <FaGoogle />   
                </div>
                <span>or use your business email for registration</span>
                <input type="text" placeholder="Name" />
                <input type="email" placeholder="Email" />
                <input type="password" placeholder="Password" />
                
                <input type="text" placeholder="Job Title" />
                <input type="text" placeholder="Start date" />
                <input type="text" placeholder="Team or Department" />
                
                <button type="button" onClick={register}>Sign Up</button>
            </form>
        </div>
        <div className="form-container sign-in-container">
            <form >
                <h1>Sign in</h1>
                <div className="social-container">
                    <FaFacebook />
                    <FaLinkedin />
                    <FaGoogle />  
                </div>
                <span>or use your business account</span>
                <input type="email" placeholder="Email" />
                <input type="password" placeholder="Password" />
                <a href="#">Forgot your password?</a>
                <Link to={'/dashboard'}>
                    <button>Sign In</button>
                </Link>
            </form>
        </div>
        <div className="overlay-container">
            <div className="overlay">
                <div className="overlay-panel overlay-left">
                    <h1>Welcome Back!</h1>
                    <p>To stay connected please login with your personal info</p>
                    <button className="ghost" id="signIn" onClick={() => toggleRegister(false)}>Sign In</button>
                </div>
                <div className="overlay-panel overlay-right">
                    <h1>Hello, Buddy!</h1>
                    <p>Enter your details and start your journey with us</p>
                    <button className="ghost" id="signUp" onClick={() => toggleRegister(true)}>Sign Up</button>
                </div>
            </div>
        </div>
    </div>
    </>
    );
}
