from flask import Flask, json, render_template, request, jsonify
from classes.manager import Manager

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question', methods=['POST'])
def handle_question():
    print("voici la question")
    question = request.form.get("user_question")
    print(request.form)
    print(request.form.get("user_question"))

    if question:
        manager = Manager(question)
        response = manager.get_response()
        return jsonify(response)
    #return jsonify({})

if __name__ == "__main__":
    app.run()