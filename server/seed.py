# server/seed.py
#!/usr/bin/env python3

from faker import Faker
from app import app
from models import db, Movie

fake = Faker()

def make_movies():
    Movie.query.delete()
    
    movies = []
    for _ in range(50):
        m = Movie(title=fake.sentence(nb_words=4).title())
        movies.append(m)

    db.session.add_all(movies)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        make_movies()
