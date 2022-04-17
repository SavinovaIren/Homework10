import json

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    with open("candidates.json", 'r', encoding='utf-8') as file:
        candidates_list = json.load(file)
    result = '<pre>'
    for candidate in candidates_list:
        result += {
            f'Имя кандидата - {candidate["name"]}\n'
            f'Позиция кандидата - {candidate["position"]}\n'
            f'Навыки через запятую - {candidate["skills"]}\n'
        }
        result += '<pre>'
    return result


@app.route("/candidates/<id>")
def candidate(id):
    pass


@app.route("/skills/<skill>")
def skill(skills):
    pass


app.run()
