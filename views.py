from flask import Flask, json, render_template, request, jsonify
from classes.manager import Manager
from classes.messages import negative_responses
from random import choice
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question', methods=['POST'])
def handle_question():
    question = json.loads(request.data.decode()).get("user_question")

    if question:
        manager = Manager(question)
        response = manager.get_response()
        return jsonify(response)
    return jsonify({"status": "nok", "message": choice(negative_responses)})

if __name__ == "__main__":
    app.run()