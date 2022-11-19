async function postCanvasContent() {
    // get data from element with id "myCanvas"
    const canvas = document.getElementById("myCanvas");
    const data = canvas.value;
    console.log(data);
    const response = await fetch('http://127.0.0.1:5000/content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}