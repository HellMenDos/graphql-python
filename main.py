from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from ariadne import gql, QueryType, MutationType, make_executable_schema, graphql_sync
from routes.users import usersSchemes
from routes.posts import postsSchemes

from schemes import type_defs,query,mutation

usersSchemes()
postsSchemes()

schema = make_executable_schema(type_defs, [query, mutation])
app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
   return PLAYGROUND_HTML

@app.route("/graphql", methods=["POST"])
def graphql_server():
   data = request.get_json()
   success, result = graphql_sync(schema, data, context_value={"request": request})
   status_code = 200 if success else 400
   return jsonify(result), status_code

if __name__ == "__main__":
   app.run(debug=True,port=3000)