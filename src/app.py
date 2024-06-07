from flask import Flask
from blog.routes.post_routes import post_routes
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(post_routes)
swagger = Swagger(app)


if __name__ == '__main__':
    app.run(debug=True)