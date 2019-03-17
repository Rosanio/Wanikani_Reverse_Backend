import React, { Component } from 'react';
import './App.css';

class App extends Component {
  
  render() {
    console.log('Start')
    fetch('http://localhost:8001/get_burned_cards')
        .then(data => {
          console.log('Got data')
          return data.json()
        })
        .then(res => {console.log(res)})
        .catch(error => {console.log(error)})
    return (
      <div className="App">
        
      </div>
    );
  }
}

export default App;
