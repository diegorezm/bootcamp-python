import requests
import html
from question_model import Question

API_URL = "https://opentdb.com/api.php"

params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(API_URL, params=params)
json = response.json()
response.close()
results = json['results']

q_list: list[Question] = [Question(type=res['type'], category=res['category'], difficulty=res['difficulty'], question=html.unescape(res['question']),correct_answer=bool(res['correct_answer']),incorrect_answers=res['incorrect_answers'][0]) for res in results]
