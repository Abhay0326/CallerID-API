import requests

url = "https://advancecaller.p.rapidapi.com/api/v1/search"

querystring = {"code":"91","number":"9811860631"}

headers = {
	"x-rapidapi-key": "4ca22833eemshf1fa94132fa310fp1ae05ajsn25cf82f09c85",
	"x-rapidapi-host": "advancecaller.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())