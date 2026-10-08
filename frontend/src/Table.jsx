import { useEffect, useState } from "react";

const URL = 'http://127.0.0.1:5000'

function Table() {

    useEffect(() => {
        const fetchData = async () => {
            const result = await fetch(URL)
            console.log(result)
        }
        fetchData();
    })

    return 
}

export default Table