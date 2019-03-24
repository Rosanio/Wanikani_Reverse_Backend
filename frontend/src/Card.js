import React, { Component } from 'react';
import './App.css';

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
    this.setState({answer: event.target.value});
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
      let answer = this.state.answer;
      let correct = (answer === this.props.card.kana ||
                     answer === this.props.card.kanji)
      this.setState({
        correct: correct,
        submitted: true
      })
    }
    event.preventDefault();
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
          <p>The correct answer was {this.props.card.kana}</p>
        </div>
      )
    }

    return (
      <div>
        <h3>{this.props.card.english}</h3>
        <form onSubmit={this.handleSubmit}>
          <input type="text" value={this.state.answer} onChange={this.handleChange} ref={this.myRef} />
          <input type="submit" value={this.state.submitted ? "Next" : "Submit"} />
        </form>
        {correctComponent}
      </div>
    )
  }
}

export default Card