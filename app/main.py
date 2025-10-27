"""Flask web application."""

from flask import Flask, request, jsonify
from flask_cors import CORS
from app import database, config, utils

app = Flask(__name__)

# TODO: Configure CORS properly
CORS(app, origins="*")


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the API"})


@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = database.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = database.search_users(query)
    return jsonify({"results": results})


@app.route("/eval", methods=["POST"])
def evaluate_expression():
    data = request.get_json()
    expression = data.get("expression", "")
    
    try:
        result = eval(expression)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=config.DEBUG, host="0.0.0.0", port=5000)
