import React, { Component } from 'react';
import Games from './components/Games'
import './App.css';

class App extends Component {
  onInput(e) {
    this.setState({
      userId: e.target.value
    })
  }
  onClick(e) {
    this.setState({ submitted: true })
  }
  render() {
    if (this.state && this.state.submitted) {
      return <Games userId={this.state.userId} />
    }
    return [
      <p key="1">What is your user ID? <input onInput={e => this.onInput(e)} /></p>,
      <button key="2" onClick={e => this.onClick(e)}>Submit</button>
    ]
  }
}

export default App;
