import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

client_id = 'f53d450d62ad475aaa44f7f0b7109ff3'      #IDs taken from Spotify my developer account
client_secret = 'd3bb12c87076424397cc2cecb4836ea9'

userName = input("Enter your username: ")  # 31am7fsjaw2rcltdcrybgt2aqerm

uri = input('Enter a playlist URI: ') # spotify:playlist:6qyJfp37a1xfvnHlDX4Jsr

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids


ids = getTrackIDs(userName, uri)


def getTrackFeatures(id):
  data = sp.track(id)
  features = sp.audio_features(id)

  # data
  name = data['name']
  album = data['album']['name']
  artist = data['album']['artists'][0]['name']
  release_date = data['album']['release_date']
  length = data['duration_ms']
  popularity = data['popularity']

  # features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']

  track = [name, album, artist, release_date, length, popularity, danceability, acousticness,
           danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track


tracks = []
for i in range(len(ids)):
  time.sleep(.5)
  track = getTrackFeatures(ids[i])
  tracks.append(track)

# create dataset
df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness',
                                   'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("spotify.csv", sep=',')
