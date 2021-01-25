# asudo aa-remove-unknownpp.py
from flask import Flask
from flask_restful import Resource, Api
from flask import request, render_template, jsonify

app = Flask(__name__)
api = Api(app)


class Artists(Resource):
	def get(self,artist):
		results=[]
		if artist:
			token = spotify.spotify_authenticate(spotify_client_id, spotify_client_secret)
			headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'Authorization': 'Bearer {}'.format(token),
			}
			results = spotify.search_by_artist_name(headers,artist)
			items = results['artists']['items']
			l=[]
			for i in items:
				genres = i['genres']
				id=i['id']
				image = i['images']
				if image!=[]:
					image = i['images'][2]['url']
				name = i['name']
				href = i['href']				
				l.append({'name':name,'genres':genres,'id':id,'image':image,'href':href})
			res = {'resultados':l,'total':len(l)}


		return jsonify(res)

api.add_resource(Artists, '/artists/<string:artist>')


import spotify


spotify_client_id = '..c10efd...e2e52...'
spotify_client_secret = '..183...bfbb8eb40a9...23'

@app.route('/', methods=['GET', 'POST'])
def index():
	token = spotify.spotify_authenticate(spotify_client_id, spotify_client_secret)
	headers = {
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'Authorization': 'Bearer {}'.format(token),
	}	
	artists={}
	if request.method == 'POST':
		artist = request.form['artist']
		if artist:
			results = spotify.search_by_artist_name(headers,artist)
			l=[]
			if results:
				items = results['artists']['items']		
				for i in items:
					genres = i['genres']
					id=i['id']
					image = i['images']
					if image!=[]:
						image = i['images'][2]['url']
					name = i['name']
					href = i['href']				
					l.append({'name':name,'genres':genres,'id':id,'image':image,'href':href})
				artists = {'resultados':l,'total':len(l)}
			print(l[0])
		
	return render_template('index.html', artists=artists)











if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    