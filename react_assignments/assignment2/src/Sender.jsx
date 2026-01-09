export default function({setMessage}) {
    return(<>
    <h3>Sender</h3>
    <input type="text" placeholder="type a message" onChange={(e)=>{setMessage(e.target.value)}}></input>
    </>);
}