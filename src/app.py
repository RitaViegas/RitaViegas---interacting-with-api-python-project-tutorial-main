import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

artist = 'spotify:artist:0PCCGZ0wGLizHt2KZ7hhA2'

results = sp.artist_top_tracks(artist, country='US')


if results:
  tracks = results["tracks"]
  #{k: v for k, v in track.items() if k in ["name", "popularity", "duration_ms"]}
  tracks = [
    {key: (value/(1000*60)) if key == "duration_ms" else value for key, value in track.items() if key in ["name", "popularity", "duration_ms"]} for track in tracks
    ]


# Convert the list of dictionaries to a Pandas DataFrame
tracks_df = pd.DataFrame(tracks)

# Sort by popularity in ascending order
tracks_df.sort_values(by= 'popularity', ascending=True)  

plt.figure(figsize=(8,6))
sns.scatterplot(data=tracks_df, x='duration_ms', y='popularity', color='purple' )


plt.title('Relationship between duration and popularity of songs')
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')


plt.show()

# Calculate the correlation between duration and popularity
correlation = tracks_df['popularity'].corr(tracks_df['duration_ms'])
print(f"Correlación entre popularidad y duración: {correlation:.2f}")



# Statistical analysis:
#  A correlation value of 0.02 between song duration and popularity indicates
#  that there is no significant linear relationship between the two variables.
#  This means that the length of a song has little to no impact on its popularity.


