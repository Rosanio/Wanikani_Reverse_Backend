import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cards: [],
      card: undefined,
      answer: ''
    };
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
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

  handleChange(event) {
    this.setState({answer: event.target.value})
  }

  handleSubmit(event) {
    console.log(this.state.answer)
    event.preventDefault()
  }

  getRandomCard(cards) {
    let index = Math.floor(Math.random() * cards.length)
    return cards[index]
  }

  render() {
    let cardComponent;
    if (this.state.card) {
      cardComponent = (
        <div>
          <h3>{this.state.card.english}</h3>
          <form onSubmit={this.handleSubmit}>
            <input type="text" value={this.state.answer} onChange={this.handleChange} />
          </form>
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
