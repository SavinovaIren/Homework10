import json


def open_candidates():
    with open("candidates.json", 'r', encoding='utf-8') as file:
        candidates_list = json.load(file)
    return candidates_list


def get_all_candidates():
    candidates_list = open_candidates()
    result = '<pre>\n'
    for candidate in candidates_list:
        result += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n'
    result += '<pre>'
    return result


def get_candidate_id(id):
    candidates_list = open_candidates()
    for candidate in candidates_list:
        if candidate["id"] == id:
            result = f'<img src = {candidate["picture"]}\n\n>'
            result += '<pre>\n'
            result += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n'
            result += '<pre>'
            return result


def get_candidate_skills(skill):
    candidates_list = open_candidates()
    result = '<pre>\n'
    for candidate in candidates_list:
        list = candidate["skills"].lower().split(", ")
        if skill in list:
            result += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n'
    result += '<pre>\n'
    return result
