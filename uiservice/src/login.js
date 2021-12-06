import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "./css/login.css";

const Login = ({loggedIn, setLoggedIn, setClientId}) => {
  const [message, setMessage] = useState(null)
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const handleSubmit = (e) => {
    e.preventDefault();

    const auth = {username, password}
    fetch("http://localhost:5000/login", {
      method: "POST",
      headers: { 'Content-Type': "application/json"},
      body: JSON.stringify(auth)
    }).then(res => res.json()).then((data) => {
      console.log(data, typeof data.logged_in);
      var logged_in = data.logged_in ? 'true' : 'false'
      sessionStorage.setItem("loggedIn", logged_in);
      setLoggedIn(logged_in);
      if (data.logged_in) {
        sessionStorage.setItem("clientId", data.client_id);
        setClientId(data.client_id)
      }
      if(data.logged_in) {
        navigate('/')
      } else {
        setMessage(data.message)
        navigate('/login')
      }
    })
  }

  return (
    <div className="pad">
      {
        loggedIn==='false' &&
        <div>
          <form onSubmit={handleSubmit}>
              <div className="form-group">
                  <label>User ID</label> <br/>
                  <input placeholder="Enter userID" value={username} onChange={(e) => setUsername(e.target.value)}/><br/>
              </div>
              <div className="form-group">
                  <label>Password</label> <br/>
                  <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/><br/>
                  <small id="emailHelp" className="form-text text-muted">We'll never share your password with anyone else.</small>
              </div>
              <div className="form-check">
                  <input type="checkbox" className="form-check-input" id="exampleCheck1"/>
                  <label className="form-check-label" htmlFor="exampleCheck1">Remember me</label>
              </div>
              <button type="submit" className="btn btn-primary">Submit</button>
          </form>
          <a href="/register">Register new user?</a><br/>
          {message}
        </div>
      }
    </div>
  );
}

  export default Login;