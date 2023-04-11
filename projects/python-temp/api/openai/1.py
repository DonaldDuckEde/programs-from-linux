import http.client

conn = http.client.HTTPSConnection("openai80.p.rapidapi.com")

payload = "{\n    \"model\": \"gpt-3.5-turbo\",\n    \"messages\": [\n        {\n            \"role\": \"user\",\n            \"content\": \"Hello!\"\n        }\n    ]\n}"

headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': "bd7537db29mshc28ea09170e58efp1afa22jsn8690e58746f2",
    'X-RapidAPI-Host': "openai80.p.rapidapi.com"
}

conn.request("POST", "/chat/completions", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
