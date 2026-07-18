import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://advancecaller.p.rapidapi.com/api/v1/search"

querystring = {"code":"91","number":"9971604367"}

headers = {
	"x-rapidapi-key": os.getenv("RAPID-API-KEY"),
	"x-rapidapi-host": "advancecaller.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())