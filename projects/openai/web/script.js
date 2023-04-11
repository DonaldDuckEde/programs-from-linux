function askQuestion() {
    const question = document.getElementById("question").value;
    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-RapidAPI-Key': 'bd7537db29mshc28ea09170e58efp1afa22jsn8690e58746f2',
            'X-RapidAPI-Host': 'openai80.p.rapidapi.com'
        },
        body: JSON.stringify({
            model: 'gpt-3.5-turbo',
            messages: [{ role: 'user', content: question }]
        })
    };
    fetch('https://openai80.p.rapidapi.com/chat/completions', options)
        .then(response => response.json())
        .then(response => {
            document.getElementById("response").innerHTML = JSON.stringify(response);
        })
        .catch(err => console.error(err));
}