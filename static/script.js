function createTeam(name, id) {
    fetch(`/create`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`card-${id}`).textContent = data;
        console.log(JSON.parse(data.split("|")[4]));
        document.getElementById(`card-${1}`).textContent = "";
        for(let i=0; i<5; i++) {
            getNeuron(JSON.parse(data.split("|")[4])[i]).then((result)=>{document.getElementById(`card-${1}`).textContent += result + ", "});
        }
    })
    .catch(err => console.error('Error:', err));
}
function getNeuron(id) {
    return fetch(`/neuron/${id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        return data
    })
    .catch(err => console.error('Error:', err));
}