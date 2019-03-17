import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cards: [],
      card: undefined,
      answer: '',
      submitted: false,
      correct: false
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
    if (this.state.submitted) {
      let newCard = this.getRandomCard(this.state.cards)
      this.setState({
        submitted: false,
        correct: false,
        card: newCard,
        answer: ''
      })
    } else {
      let correct = (this.state.answer === this.state.card.kana ||
                     this.state.answer === this.state.card.kanji)
      this.setState({
        correct: correct,
        submitted: true
      })
    }
    event.preventDefault()
  }

  getRandomCard(cards) {
    let index = Math.floor(Math.random() * cards.length)
    return cards[index]
  }

  render() {
    let cardComponent;
    let correctComponent;
    if (this.state.card) {
      cardComponent = (
        <div>
          <h3>{this.state.card.english}</h3>
          <form onSubmit={this.handleSubmit}>
            <input type="text" value={this.state.answer} onChange={this.handleChange} />
            <input type="submit" value={this.state.submitted ? "Next" : "Submit"} />
          </form>
        </div>
      )
    } else {
      cardComponent = <h3>Loading...</h3>
    }

    if (!this.state.submitted) {
      correctComponent = <div></div>
    } else if (this.state.correct) {
      correctComponent = <div><p>Correct!</p></div>
    } else {
      correctComponent = (
        <div>
          <p>Incorrect Answer</p>
          <p>The correct answer was {this.state.card.kana}</p>
        </div>
      )
    }
    
    return (
      <div className="App">
        <h1>WaniKani Reverse</h1>
        {cardComponent}
        {correctComponent}
      </div>
    );
  }
}

export default App;
