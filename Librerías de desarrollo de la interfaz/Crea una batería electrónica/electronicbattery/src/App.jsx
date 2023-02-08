import './App.css'
import { useEffect } from 'react';

function handleKeyPress(e) {
  console.log(e.key);

  if (e.key === 'a') {
    var audio = new Audio('../assets/Heater-1.mp3');
    audio.play();
  } else if (e.key === 's') {
    var audio = new Audio('../assets/Heater-2.mp3');
    audio.play();
  } else if (e.key === 'd') {
    var audio = new Audio('../assets/Heater-3.mp3');
    audio.play();
  } else if (e.key === 'f') {
    var audio = new Audio('../assets/Heater-4.mp3');
    audio.play();
  }
}

function App() {  
  useEffect(() => {
    document.addEventListener('keydown', handleKeyPress);

    return () => {
      document.removeEventListener('keydown', handleKeyPress);
    };
  }, [handleKeyPress]);

  return (
    <div className="App">      
      <div className="card">
        <button onClick={() => {
          var audio = new Audio('../assets/Heater-1.mp3');
          audio.play();}}>A
        </button>
        <button onClick={() => {
          var audio = new Audio('../assets/Heater-2.mp3');
          audio.play();}}>S
        </button>
        <button onClick={() => {
          var audio = new Audio('../assets/Heater-3.mp3');
          audio.play();}}>D
        </button>
        <button onClick={() => {
          var audio = new Audio('../assets/Heater-4.mp3');
          audio.play();}}>F
        </button>
      </div>
      <p className="doneBy">
        by PhotographyRaptor
      </p>
    </div>
  )
}

export default App
