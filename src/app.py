import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
con = spotipy.Spotify(auth_manager=auth_manager)

artist_id = "0PCCGZ0wGLizHt2KZ7hhA2"
artist = 'spotify:artist:0PCCGZ0wGLizHt2KZ7hhA2'


response = sp.artist_top_tracks("0PCCGZ0wGLizHt2KZ7hhA2")
if response:
  # We keep the "tracks" object of the answer
  tracks = response["tracks"]
  # We select, for each song, the data we are interested in and discard the rest
  tracks = [{k: (v/(1000*60))%60 if k == "duration_ms" else v for k, v in track.items() if k in ["name", "popularity", "duration_ms"]} for track in tracks]
