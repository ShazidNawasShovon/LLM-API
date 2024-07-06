import requests

url = 'http://127.0.0.1:5000/evaluate'

data = [
    {
        'answer_1': 'The cat is on the mat.',
        'answer_2': 'There is a cat on the mat.',
        'answer_3': 'A cat is sitting on a mat.',
        'answer_4': 'On the mat, there is a cat.',
        "question": "Where is the cat?",
        'student_answer': 'A cat is on the mat.'
    },
    # Add more student answers here if needed
]

response = requests.post(url, json=data)
print(response.json())
