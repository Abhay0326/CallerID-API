import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://truecaller-data2.p.rapidapi.com/search/919599659909"

headers = {
	"x-rapidapi-key": os.getenv("RAPID-API-KEY"),
	"x-rapidapi-host": "truecaller-data2.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())