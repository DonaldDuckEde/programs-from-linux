import http.client

conn = http.client.HTTPSConnection("openai80.p.rapidapi.com")

payload = "{\n    \"model\": \"gpt-3.5-turbo\",\n    \"messages\": [\n        {\n            \"role\": \"user\",\n            \"content\": \"Hello!\"\n        }\n    ]\n}"

headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': "own API key",
    'X-RapidAPI-Host': "openai80.p.rapidapi.com"
}

conn.request("POST", "/chat/completions", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
