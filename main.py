import json

from flask import Flask

with open("candidates.json", 'r', encoding='utf-8') as file:
    candidates_list = json.load(file)

app = Flask(__name__)


@app.route("/")
def main_page():
    result = '<pre>\n'
    for candidate in candidates_list:
        result += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n'
    result += '<pre>'
    return result


@app.route("/candidates/<int:id>")
def candidate(id):
    for candidate in candidates_list:
        if candidate["id"] == id:
            result = f'<img src = {candidate["picture"]}\n\n>'
            result += '<pre>\n'
            result += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n'
            result += '<pre>'
            return result


@app.route("/skills/<skill>")
def skill(skill):
    result = '<pre>\n'
    for candidate in candidates_list:
        list = candidate["skills"].lower().split(", ")
        if skill in list:
            result += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n'
    result += '<pre>\n'
    return result


app.run()