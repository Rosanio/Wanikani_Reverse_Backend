import React, { Component } from 'react';
import './App.css';
let wanakana = require('wanakana')

class Card extends Component {
  constructor(props) {
    super(props);
    this.state = {
      answer: '',
      submitted: false,
      correct: false
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.myRef = React.createRef();
  }

  handleChange(event) {
    let kana = wanakana.toKana(event.target.value, {IMEMode: true})
    this.setState({answer: kana});
  }

  handleSubmit(event) {
    if (this.state.submitted) {
      this.setState({
        submitted: false,
        correct: false,
        answer: ''
      })
      this.props.onCardAnswered();
    } else {
      this.setState({
        correct: this.isCorrectAnswer(),
        submitted: true
      })
    }
    event.preventDefault();
  }

  isCorrectAnswer() {
    let answer = this.state.answer;
    return (answer === this.props.card.kana ||
                   answer === this.props.card.kanji)
  }

  render() {
    let correctComponent;

    if (!this.state.submitted) {
      correctComponent = <div></div>
    } else if (this.state.correct) {
      correctComponent = <div><p>Correct!</p></div>
    } else {
      correctComponent = (
        <div>
          <p>Incorrect Answer</p>
          <p>The correct answer was {this.props.card.kana} ({this.props.card.kanji})</p>
        </div>
      )
    }

    return (
      <div>
        <h3>{this.props.card.english}</h3>
        <form onSubmit={this.handleSubmit}>
          <input type="text" value={this.state.answer} onChange={this.handleChange} ref={this.myRef} id='answer' />
          <input type="submit" value={this.state.submitted ? "Next" : "Submit"} id='submit-answer' />
        </form>
        {correctComponent}
      </div>
    )
  }
}

export default Card