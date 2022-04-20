from pprint import pprint

import requests
from bs4 import BeautifulSoup
import unicodedata
import spotipy
from numpy import all


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")


CLIEND_ID = "9279***********************6dfb0"
CLIEND_SECRET = "82d5***********************8b0a4"
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'
MAIN_URL = "https://www.billboard.com/charts/hot-100/"
REDIRECT_URI = "https://example.com"
date = input("Input date in YYYY-MM-DD format:")
url = f"{MAIN_URL}{date}/"

rqst = requests.get(url)

soup = BeautifulSoup(rqst.text, features="html.parser")
all_song_tags = soup.find_all(name="h3", id="title-of-a-story", class_="a-truncate-ellipsis", attrs="")


song_names = [f"track: {remove_control_characters(h3.text)} year: {date.split('-')[0]}" for h3 in all_song_tags]

spty_o_auth = spotipy.SpotifyOAuth(client_id=CLIEND_ID, client_secret=CLIEND_SECRET,
                                   redirect_uri=REDIRECT_URI, scope="playlist-modify-private")
access_token = spty_o_auth.get_access_token(as_dict=False)

client = spotipy.Spotify(auth=access_token)
user_curr = client.current_user()
user_id = user_curr["id"]
URIs = []
for song in song_names:
    try:
        URIs.append(client.search(q=song, limit=1, type="track", )['tracks']['items'][0]['uri'])
    except spotipy.SpotifyException:
        continue
    except IndexError:
        continue

new_playlist = client.user_playlist_create(user=user_id, name=f"{date} Bilboard 100", public=False, description='')
playlist_id = new_playlist["id"]
appending_res = client.playlist_add_items(playlist_id=playlist_id, items=URIs)
