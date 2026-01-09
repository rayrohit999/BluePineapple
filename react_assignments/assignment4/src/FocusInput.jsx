import {useRef} from 'react';

export default function FocusInput() {
    //creating a ref for the input element
    const inputRef = useRef(null);

    //function to handle focus
    const handleFocus = () => {
        inputRef.current.focus();
    }

    return(
        <div>
            <h2>useRef example</h2>

            {/* attaching ref to input field */}
            <input type="text" placeholder="click button to focus me" ref={inputRef}></input>

            <br/><br/>
            <button onClick={handleFocus}>Focus Input</button>
        </div>
    );
}