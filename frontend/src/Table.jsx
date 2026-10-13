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
        <div className = "table">
            <table>
                <tr>
                    <th>Name</th>
                    <th>Category</th>
                    <th>Difficulty</th>
                    <th>Date Solved</th>
                </tr>
                {problems.map((problem) => (
                    <tr key={problem.id}>
                        <td>{problem.problem_name}</td>
                        <td>{problem.category}</td>
                        <td>{problem.difficulty}</td>
                        <td>{problem.date_solved}</td>
                    </tr>
                ))}
            </table>
        </div>
    );
}

export default Table