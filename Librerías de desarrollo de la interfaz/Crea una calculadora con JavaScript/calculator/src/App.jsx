import './App.css'
import React from 'react'

function calc(hist) {
  let total = 0;
  let sums = hist.split('+')
  console.log("sums");
  for(let sum in sums) {
    let rests = sum.split('-')
    let r = 0;
    console.log("rests");
    for(let rest in rests) {
      let divs = rest.split('/')
      let d = 1;
      console.log("divs");
      for(let div in divs) {
        let mults = div.split('X')
        let m = 1;
        console.log("mults");
        for(let mult in mults) {
          mult = mult == 0 ? 1: mult;
          m = m * mult;
          console.log("m".concat(">").concat(m.toString()));
        }
        d = d / m;
        console.log("d".concat(">").concat(d.toString()));
      }
      r = r - d;
      console.log("r".concat(">").concat(r.toString()));
    }
    total = total + r;
    console.log("s".concat(">").concat(total.toString()));
  }
  return total;
}


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      historic: "",
      value: ""
    };
  }

  handleClick = (v) => {
    console.log(v.toString());
    console.log(this.state);
    let hist = "";
    let val = "";

    if (v == "AC") {
    } else if (v == "/" || v == "X" || v == "-" || v == "+") {
      hist = this.state.historic + v;
    } else if (v == "1" || v == "2" || v == "3" 
      || v == "4" || v == "5" || v == "6" || v == "."
      || v == "7" || v == "8" || v == "9" || v == "0") {
      hist = this.state.historic.concat(v.toString());
    } else if (v == "=") {
      //hist = this.state.historic + v;
      val = calc(hist);
      //hist = hist + ' = ' + val;
    }
    
    this.setState({
      historic: hist,
      value: val
    });
    console.log(this.state.historic);
    console.log(this.state.val);
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
