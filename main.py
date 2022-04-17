import json

from apps import get_all_candidates, get_candidate_id, get_candidate_skills

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    return get_all_candidates()

@app.route("/candidates/<int:id>")
def candidate(id):
    return get_candidate_id(id)


@app.route("/skills/<skill>")
def skill(skill):
    return get_candidate_skills(skill)


app.run()