
import sys
import requests

API_KEY = "043cf95d6921576d9bb787ba33688784d47bde34d954a2db33a0bc975921XXXX"
URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    n = float(sys.argv[1])
except:
    sys.exit("Wrong number!")


try:
    response = requests.request("GET", URL)
except:
    print("Error!")
else:
    print(f"{float(response.json()["data"]["priceUsd"]) * n:.4n}")