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
    })
    .catch(error => {console.log(error)})
  }

  getRandomCard() {
    let index = Math.floor(Math.random() * this.state.cards.length)
    return this.state.cards[index]
  }

  render() {
    let card;
    let cardComponent;
    if (this.state.cards.length > 0) {
      card = this.getRandomCard();
      cardComponent = (
        <div>
          <h3>{card.english}</h3>
        </div>
      )
    } else {
      cardComponent = <h3>Loading...</h3>
    }
    
    return (
      <div className="App">
        <h1>WaniKani Reverse</h1>
        {cardComponent}
      </div>
    );
  }
}

export default App;
