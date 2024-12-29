import os

import requests
from dotenv import load_dotenv


load_dotenv()


def get_wheather(city: str = "Neratovice"):
    api_key = os.getenv("a6d53a9618f040caa60193244242912")
    url = f"https://api.weatherapi.com/v1/current.json?q={city}&key={api_key}"
    response = requests.get(url).json()
    wheather = {
        "temp": response.get("current", {}).get("temp_c"),
        "text": response.get("current", {}).get("condition", {}).get("text"),
        "icon": response.get("current", {}).get("condition", {}).get("icon"),
        "city": city
    }
    return wheather
