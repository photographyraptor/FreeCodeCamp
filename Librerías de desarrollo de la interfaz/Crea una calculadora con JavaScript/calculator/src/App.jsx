import './App.css'
import React from 'react'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      historic: "",
      value: ""
    };
  }

  handleClick = (v) => {
    console.log(v);
    console.log(this.state);
    let hist = "";
    let val = "";

    switch (v) {
      case "AC":
        break;
      case "/","X","-","+":
        hist = this.state.historic + v;
        break;
      case "1","2","3","4","5","6","7","8","9","0",".":
        hist = this.state.historic + v;
        break;
      case "=":
        hist = this.state.historic + v;
        val = "CALC"
        hist = hist + ' ' + val;
        break;
      default:
        break;
    }

    console.log('hist -> ' + hist);
    console.log('val -> ' + val)
    this.setState({
      historic: hist,
      value: val
    });
  };

  render () {
    return (
      <div className="App">
        <div className="card">
          <p className="historic"></p>
          <p className="value"></p>
          <button onClick={this.handleClick.bind(this, "AC")}>AC</button>
          <button onClick={this.handleClick.bind(this, "/")}>/</button>
          <button onClick={this.handleClick.bind(this, "X")}>X</button>

          <button onClick={this.handleClick.bind(this, "7")}>7</button>
          <button onClick={this.handleClick.bind(this, "8")}>8</button>
          <button onClick={this.handleClick.bind(this, "9")}>9</button>
          <button onClick={this.handleClick.bind(this, "-")}>-</button>

          <button onClick={this.handleClick.bind(this, "4")}>4</button>
          <button onClick={this.handleClick.bind(this, "5")}>5</button>
          <button onClick={this.handleClick.bind(this, "6")}>6</button>
          <button onClick={this.handleClick.bind(this, "+")}>+</button>

          <button onClick={this.handleClick.bind(this, "1")}>1</button>
          <button onClick={this.handleClick.bind(this, "2")}>2</button>
          <button onClick={this.handleClick.bind(this, "3")}>3</button>
          <button onClick={this.handleClick.bind(this, "=")}>=</button>

          <button onClick={this.handleClick.bind(this, "0")}>0</button>
          <button onClick={this.handleClick.bind(this, ".")}>.</button>
        </div>
        <p className="doneBy">
          by PhotographyRaptor
        </p>
      </div>
    );
  }
}

export default App
