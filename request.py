import requests
import secrets

endpoint = "https://api.spotify.com/v1/me/player/recently-played?limit=5"

header = {
    'Authorization': 'Bearer %s' % secrets.access_token,
}


r=requests.get(endpoint, headers=header);

# print(r.json())
response_data = r.json()

print(response_data.keys())

tracks = response_data.get("items")

n = response_data.get('cursors')
i = 1
if tracks:
    for t in tracks:
        track = t.get('track')
        after = t.get('played_at')
        print(str(i) + ": " + track.get('name'))
        # print(track.get())
        i+=1
print(n)
# while(i < 200):
#     endpoint = "https://api.spotify.com/v1/me/player/recently-played?limit=50&after=" + after
#
#     header = {
#         'Authorization': 'Bearer %s' % secrets.access_token,
#     }
#
#
#     r=requests.get(endpoint, headers=header);
#
#     print(r.json())
#
#     tracks = r.json().get("items")
#
#     if tracks:
#         for t in tracks:
#             track = t.get('track')
#             after = t.get('played_at')
#             print(str(i) + ": " + track.get('name'))
#             print(track.get())
#             i+=1
