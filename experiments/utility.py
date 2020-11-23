import requests


def get_answer(question, context):
    r = requests.post("http://127.0.0.1:5000/answer", json={'context': context, 'question': question})
    return r.text
