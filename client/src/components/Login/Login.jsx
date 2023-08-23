import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';
import './Login.css';


import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
} from 'mdb-react-ui-kit';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();
  const [loginFailed, setLoginFailed] = useState(false);

  const escapeHtml = (unsafe) => {
    return unsafe.replace(/</g, '&lt;').replace(/>/g, '&gt;');
  };

  const handleLogin = async () => {

    const sanitizedUsername = escapeHtml(username);
    const sanitizedPassword = escapeHtml(password);

    try {
      const response = await axios.post('http://localhost:5000/login', {
        username: sanitizedUsername,
        password: sanitizedPassword,
      });

      

      if (response.data.success) {
        const token = response.data.token;
        const userId = response.data.user_id;
        const userRole = response.data.user_role;
        console.log(token);
        console.log(userId);
        console.log(userRole);
        localStorage.setItem('authToken', token);
        localStorage.setItem('userId', userId);
        localStorage.setItem('userRole', userRole);
        history.push('/students');
      } else {
        setLoginFailed(true);
      }
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  return (
    <MDBContainer fluid>
      <MDBRow className='d-flex justify-content-center align-items-center h-100'>
        <MDBCol col='12'>
          <MDBCard
            className='bg-dark text-white my-5 mx-auto'
            style={{ borderRadius: '1rem', maxWidth: '400px' }}
          >
            <MDBCardBody
              className='p-5 d-flex flex-column align-items-center mx-auto w-100'
            >
              <h2 className='fw-bold mb-2 text-uppercase' style={{ color: 'white' }}>Login</h2>

              <p className='text-white-50 mb-5'>
                Enter your username and password
              </p>
              <input
                    className="login-input"
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
               />
                <input
                        className="login-input"
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                />

                {loginFailed && (
                    <p className="login-error">Login failed. Please check your username and password.</p>
                )}
            
            <button className="login-button" onClick={handleLogin}>Login</button>

              
            </MDBCardBody>
          </MDBCard>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
};

export default Login;
