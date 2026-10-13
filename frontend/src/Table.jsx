import { useEffect, useState } from "react";

const URL = "http://127.0.0.1:5000/api/problems/";

function Table() {

    const [problems, setProblems] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await fetch(URL);
            const data = await result.json();
            
            console.log(data);
            setProblems(data);
        }
        fetchData();
    }, []);

    return (
        <div>
            {/* Your table will go here */}
        </div>
    );
}

export default Table