import requests

url = "https://truecaller-data2.p.rapidapi.com/search/919999999999"

headers = {
	"x-rapidapi-key": "4ca22833eemshf1fa94132fa310fp1ae05ajsn25cf82f09c85",
	"x-rapidapi-host": "truecaller-data2.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())