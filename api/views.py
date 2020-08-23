from flask import Blueprint, jsonify, request
from . import db
from .models import Movie

main1 = Blueprint('main1', __name__)  # main1 is just a name given to the blueprint


@main1.route('/add_movies', methods=['POST'])  # we create a POST endpoint of url /add_movies
def add_movie():  # This endpoint adds items to the db
    movie_data = request.get_json()  # request sent to this endpoint
    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])
    db.session.add(new_movie)
    db.session.commit()

    return 'Done', 201


@main1.route('/movies', methods=['GET'])  # we create a GET endpoint of url /movies
def movies():
    list_of_movies = Movie.query.all()  # of type query
    movies = []
    for movie in list_of_movies:
        movies.append({'id': movie.id, 'title': movie.title, 'rating': movie.rating})
    return jsonify({'movies': movies})


'Below we build a URL dynamically'
@main1.route('/showName/<name>') # being shown on back-end port
def show_name(name):
    return 'Hey' + name


#  add_movie() gets JSON

#  movies() returns JSON
