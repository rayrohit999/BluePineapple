import './App.css';
import {useState} from 'react';
function App() {
  const [count, setCount] = useState(0);
  return (
   <>
    <h3>Count: {count}</h3>
    <button onClick={()=>setCount(count + 1)}>+</button>
    <button onClick={()=>setCount(count - 1)}>-</button>
   </>
  );
}

export default App;
