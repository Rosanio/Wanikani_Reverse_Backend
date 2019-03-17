import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cards: []
    };
  }

  componentDidMount() {
    fetch('http://localhost:8001/get_burned_cards')
    .then(data => {return data.json()})
    .then(res => {
      this.setState({
        cards: res
      })
      console.log(this.state)
    })
    .catch(error => {console.log(error)})
  }

  render() {
    return (
      <div className="App">
        
      </div>
    );
  }
}

export default App;
