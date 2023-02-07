import { useState } from 'react'
import './App.css'

function App() {  
  const [index, nextPhrase] = useState(0)
  const quotes = {
    "Don't explain your philosophy. Embody it": "Epictus",
    "It is the obvious which is so difficult to see most of the time. People say 'It's as plain as the nose on your face.' But how much of the nose on your face can you see, unless someone holds a mirror up to you?": "Isaac Asimov",
    "I have studied many philosophers and many cats. The wisdom of cats is infinitely superior.": "Hippolyte A. Taine",
    "A foolish consistency is the hobgoblin of little minds.": "Ralph Waldo Emerson",
    "Of what use is a philosopher who doesn't hurt anybody's feelings?": "Diogenes of Sinope",
    "They say philosophers and wise men are indifferent. Wrong. Indifference is a paralysis of the soul, a premature death.": "Anton Chekhov",
    "Dogs and philosophers do the greatest good and get the fewest rewards.": "Diogenes of Sinope",
    "Poets are the sense, philosophers­­ the intelligence­­ of humanity.": "Samuel Beckett",
    "Many men talk like philosophers and live like fools.": "Philip K. Dick",
    "Keep those that influence you for the better close and never give them a reason to keep you far away.": "Shannon L. Alder",
    "Philosophers tell you what they think. Artists show you.": " Marty Rubin"
  };

  return (
    <div className="App">
      <div className="card">
        <p className="startq">"</p>
        <p className="quote">{Object.keys(quotes)[index]}</p>
        <p className="author">- {Object.values(quotes)[index]}</p>        
        <button className="buttonCard" onClick={() => {
          nextPhrase(Math.floor(Math.random() * Object.keys(quotes).length));
          const color1 = Math.floor(Math.random() * 255);
          const color2 = Math.floor(Math.random() * 255);
          const color3 = Math.floor(Math.random() * 255);
          const root = document.querySelector('#root');
          root.style.setProperty('--main-color', 'rgb(' + color1 + ',' + color2 + ',' + color3 + ')');
          const root2 = document.querySelector(':root');
          root2.style.setProperty('--main-color', 'rgb(' + color1 + ',' + color2 + ',' + color3 + ')');
        }}>Next quote
        </button>
      </div>
      <p className="doneBy">
        by PhotographyRaptor
      </p>
    </div>
  )
}

export default App
