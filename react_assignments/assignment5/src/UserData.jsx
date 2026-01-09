import {useState, useEffect} from "react";

export default function UserData() {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function fetchData() {
            try{
                const response = await fetch("https://jsonplaceholder.typicode.com/users");
                const user = await response.json();
                setUser(user[0]);
            }catch(error) {
                setError(error.message);
            }finally {
                setLoading(false);
            }
        }
        fetchData();

    },[]);

    if(loading) return <p>Loading....</p>;
    if(error) return <p>Error: {error}</p>;

    return(
        <div>
            <h2>User Details</h2>
            <p>Name: {user.name}</p>
            <p>Email: {user.email}</p>
        </div>
    );
}