"""there was an error 'FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead
and will be disabled by default i n the future. Set it to True or False to suppress this warning.'

I resoved it by 'app.config.setdefault('SQLALCHEMY_COMMIT_ON_TEARDOWN', False)' """
"""
"""

"""
Start the front end:

1- Have backend running on port 5000
2- check for both node and npx installed "node -v" and "npx --version"
3- npx create-react-app front-end
4- go to front-end and npm start
5 - for this project i install 
by "npm i semantic-ui-react semantic-ui-css"


Now open React.JS:

1- add a proxy to package.json bc whenever we make a request fetch("/") proxies it to the right server
2- components folder must be inside the src
"""

"""
    FLASK_DEBUG=1 ==>  The server will then reload itself (not manually) if the code changes.
    The route() decorator of a Flask object is used to bind URL to a function
    An object of Flask class is our WSGI application app = Flask(__name__) # 
        A Web Server Gateway Interface (WSGI) server implements the web server side of the 
        WSGI interface for running Python web applications.
    


"""