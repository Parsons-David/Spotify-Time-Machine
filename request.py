import requests
import secrets

endpoint = "https://api.spotify.com/v1/me/player/recently-played"

header = {
    'Authorization': 'Bearer %s' % secrets.access_token,
}


r=requests.get(endpoint, headers=header);

print(r.json())
