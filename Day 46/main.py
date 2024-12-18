import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

header = {
    'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'

}

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        # client_id='fcae1ba11be04009b798092c342aeb9a',
        # client_secret='f551f5817b634f88a06de3ec30a3a960',
        show_dialog=True,
        cache_path="/Users/danny714/Desktop/Python/Day 46/token.txt"
    )
)

user_id = sp.current_user()["id"]

# playlists = sp.user_playlists(user_id)

# for item in playlists['items']:
#     print(item['name'], item['id'])


date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

created_playlist = sp.user_playlist_create(
    user_id, f'{date} Billboard 100', public=False, description='top 100 billboard')

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=created_playlist["id"], items=song_uris)
