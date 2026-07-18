import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://eyecon.p.rapidapi.com/api/v1/search"

querystring = {"code":"91","number":"8368775338"}

headers = {
	"x-rapidapi-key": os.getenv("RAPID-API-KEY"),
	"x-rapidapi-host": "eyecon.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())