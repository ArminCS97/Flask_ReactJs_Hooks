"""Pay attention to 2 parts below the cummented part and the non-commnted part are equivalent A and B.
The difference between them is that in A we need to set 2 variables using the terminal set FLASK_APP=api (main directory)
and set FLASK_DEBUG=1  however in B we can run it using pycharm. The other difference is that A shows the JSON on the page better
vertically I mean but B shows horizontally. A IS PREFERRED. To make A run type "flask run".


The other important point is that order of creating app and db really matters"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""A [ """
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    from .views import main1
    from .views_award import main2

    app.register_blueprint(main1, url_prefix='/')
    # app.register_blueprint(main2)

    return app


""" ] A"""



"""B [ """
# db = SQLAlchemy() # 1 define db
#
# app = Flask(__name__) # 2 create the app
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # 3 config the app database
# db.init_app(app) # 4 initialize the database by our app created
#
# from .views import main1
# app.register_blueprint(main1)
#
# if __name__ == '__main__':
#     app.run(debug=1)

"""] B"""
