import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  
  render() {
    fetch('http://localhost:5000/get_burned_cards')
        .then(data => {return data.json()})
        .then(res => {console.log(res)})
    return (
      <div className="App">
        
      </div>
    );
  }
}

export default App;
