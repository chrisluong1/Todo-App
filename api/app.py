from flask import Flask
from flask_graphql import GraphQLView
from models import session
from schema import schema
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)


app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


if __name__ == "__main__":
    app.run()
