import requests

url = "https://eyecon.p.rapidapi.com/api/v1/search"

querystring = {"code":"91","number":"8368775338"}

headers = {
	"x-rapidapi-key": "4ca22833eemshf1fa94132fa310fp1ae05ajsn25cf82f09c85",
	"x-rapidapi-host": "eyecon.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())