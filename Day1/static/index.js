let api_call = async() => {
    let res = await fetch("http://127.0.0.1:5000/students/new",
        {
            method:"POST",
            contentType: "application/json",
            body: JSON.stringify({ "name": "kashif", "id":"1" })
        }
    );
    if(res.status===200) {
        console.log("hurrayyy");
        let data = await res.json();
        console.log(data);
    }
    else {
        console.log("damn");
    }
}
