import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask

from flask_restplus import Api, Resource
app = Flask(__name__)
api = Api(app)
@api.route('/hello/')
class HelloWorld(Resource):
    def get(self):
        return "Hello World"
    
if __name__ == '__main__':
    app.run()