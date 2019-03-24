import React, { Component } from 'react';
import './App.css';
import Card from './Card.js';
let wanakana = require('wanakana')

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cards: [],
      card: undefined
    };
    this.onCardAnswered = this.onCardAnswered.bind(this);
  }

  componentDidMount() {
    console.log(this.myRef)
    fetch('http://localhost:8001/get_burned_cards')
    .then(data => {return data.json()})
    .then(res => {
      this.setState({
        cards: res,
        card: this.getRandomCard(res)
      })
    })
    .catch(error => {console.log(error)})
  }

  onCardAnswered() {
    let newCard = this.getRandomCard(this.state.cards)
    this.setState({
      card: newCard
    })
  }

  getRandomCard(cards) {
    let index = Math.floor(Math.random() * cards.length)
    return cards[index]
  }

  render() {
    let cardComponent;
    if (this.state.card) {
      cardComponent = <Card card={this.state.card} onCardAnswered={this.onCardAnswered} />
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
