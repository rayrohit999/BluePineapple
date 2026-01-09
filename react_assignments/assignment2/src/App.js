import './App.css';
import Sender from './Sender';
import Reciver from './Reciver';
import {useState} from 'react';
function App() {
  const [message, setMessage] = useState("");
  return (
    <div>
      <h2>Passing data between sibling components</h2>
      <Sender setMessage={setMessage}/> {/*Pssing setter to sender */}
      <Reciver message={message}/> {/* Passing data to Reciver */}
    </div>
  );
}

export default App;
