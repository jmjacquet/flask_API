import requests

GET_ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
RELATED_ARTISTS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/related-artists'
TOP_TRACKS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/top-tracks'

# https://developer.spotify.com/web-api/get-artist/



def get_artist(headers,artist_id):
    url = GET_ARTIST_ENDPOINT.format(id=artist_id)
    resp = requests.get(url,headers=headers)
    return resp.json()


# https://developer.spotify.com/web-api/search-item/
def search_by_artist_name(headers,name):
    myparams = {'type': 'artist'}
    myparams['q'] = name
    resp = requests.get(SEARCH_ENDPOINT, headers=headers,params=myparams)
    return resp.json()


# https://developer.spotify.com/web-api/get-related-artists/
def get_related_artists(headers,artist_id):
    url = RELATED_ARTISTS_ENDPOINT.format(id=artist_id)
    resp = requests.get(url,headers=headers)
    return resp.json()

# https://developer.spotify.com/web-api/get-artists-top-tracks/
def get_artist_top_tracks(headers,artist_id, country='US'):
    url = TOP_TRACKS_ENDPOINT.format(id=artist_id)
    myparams = {'country': country}
    resp = requests.get(url, params=myparams,headers=headers)
    return resp.json()


def spotify_authenticate(spotify_client_id, spotify_client_secret):
    data = {'grant_type': 'client_credentials'}
    url = 'https://accounts.spotify.com/api/token'
    response = requests.post(url, data=data, auth=(spotify_client_id, spotify_client_secret))
    return response.json()['access_token']    