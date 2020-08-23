from flask import Blueprint, jsonify, request
from . import db
from .models import Award

main2 = Blueprint('main2', __name__)


@main2.route('/add_awards', methods=['POST'])
def add_awards():
    award_data = request.get_json()
    new_award = Award(movie=award_data['movie'], award_name=award_data['award_name'])
    db.session.add(new_award)
    db.session.commit()

    return 'Done', 201


@main2.route('/awards', methods=['GET'])
def awards():
    awards_list = Award.query.all()
    awards = []
    for a in awards_list:
        awards.append({'id': a.id, 'movie': a.movie, 'award_name':a.award_name})
    return jsonify({'awards': awards})


"""The basic concept of blueprints is that they record operations to execute when registered on an application. 
Flask associates view functions with blueprints when dispatching requests and generating URLs from one endpoint to another."""