import React from 'react';

const NavBar = () =>  {

  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <a className="navbar-brand" href="/">FooFi</a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item">
              <a className="nav-link" href="/restaurants">Restaurants</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/analytics">Analytics</a>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
}

export default NavBar;