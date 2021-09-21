import React, { useState } from "react";
import validator from 'validator';
import './email.styles.scss';
  
const EmailField = () => {
  
  const [emailError, setEmailError] = useState('')
  const validateEmail = (e) => {
    var email = e.target.value
  
    if (validator.isEmail(email)) {
      setEmailError('Valid Email :)')
    } else {
      setEmailError('Enter valid Email!')
    }
  }
  
  return (
    <div className='email'>
      <pre>
        <h2 className='heading'>Subscribe Using Your Email Address</h2>
        <span>Enter Email: </span><input className = 'field'size ='large' type="text" id="userEmail" 
        onChange={(e) => validateEmail(e)}></input> <br />
        <span style={{
          fontWeight: 'bold',
          color: 'red',
        }}>{emailError}</span>
        <button>Submit</button>
      </pre>
    </div>
  );
}
export default EmailField;