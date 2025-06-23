# server/app.py
#!/usr/bin/env python3

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/movies', methods=['GET'])
def movies():
    movies = Movie.query.all()
    movie_list = [movie.to_dict() for movie in movies]

    return make_response(jsonify(movie_list), 200)

if __name__ == '__main__':
    app.run(port=5555)
