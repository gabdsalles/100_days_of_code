import requests, os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


URL = "https://www.billboard.com/charts/hot-100/"
ID_CLIENT = os.environ.get("ID_CLIENT")
SECRET = os.environ.get("SECRET")
print(ID_CLIENT)
print(SECRET)

date = input("Pra que ano vc quer viajar? Digite a data no formato YYYY-MM-DD: ")

response = requests.get(f"{URL}{date}")

soup = BeautifulSoup(response.text, "html.parser")

songs_name = soup.select(selector="li h3", class_="c-title")
songs_list = []
 
for song in songs_name:
    text = song.getText().strip()
    if len(songs_list) < 100:
        songs_list.append(text)
 
#print(songs_list)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:4304/auth/spotify/callback",
        client_id=ID_CLIENT,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="./Day 46 - Beautiful Soup + Spotify API/token.txt",
        username='31czjxj5pgyhjvprnz24a2fdljgy', 
    )
)

user_id = sp.current_user()["id"]

song_uris = []

for song in songs_list:
    
    result = sp.search(q=f"track:{song} year:{2002}", type="track")
    #pprint.pp(result)
    
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)


sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Playlist criada com sucesso!")