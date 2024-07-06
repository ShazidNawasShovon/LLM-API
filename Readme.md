# Project Setup Instructions 
#### [Click here to see the Setup Instructions](https://shazidnawasshovon.github.io/LLM-API/)

LLM Project is a Python library Model for dealing with word pluralization.

#### 1. Install Dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Project.

```bash
pip install -r requirements.txt
```
* This installs all required Python packages listed in `requirements.txt`, including Flask, pandas, transformers, sentence-transformers, and others.

#### 2. Prepare CSV File (if applicable)
* Ensure the CSV file (`Demo Data 1 - Sheet1.csv`) is placed in the root directory of the project or specify the correct path.
#### 3. Run the Flask Application
* Open a `Terminal` in VS Code then paste.
```bash

python app.py # run with CSV file

python app_without_CSV.py # run without CSV file

```
* This command starts the Flask server. By default, it runs on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

#### 4. Access the API

* Once the Flask application is running, you can access the following endpoints:
  * /: Provides information about the home page and how to use the API.
  * /evaluate: Endpoint for evaluating student answers. Send POST requests with JSON data to this endpoint.
## Usage:

```python

import requests

url = 'http://127.0.0.1:5000/evaluate'

data = [
    {
        'answer_1': 'The cat is on the mat.',
        'answer_2': 'There is a cat on the mat.',
        'answer_3': 'A cat is sitting on a mat.',
        'answer_4': 'On the mat, there is a cat.',
        'student_answer': 'A cat is on the mat.'
    },
    # Add more student answers here
]

response = requests.post(url, json=data)
print(response.json())

```
#### 3. Run the API in Terminal
* Open another `Terminal` in VS Code then paste.
```bash
python test_api.py
```

## Using Postman:

##### 1. Open Postman.
##### 2. Set the request type to POST.
##### 3. Enter http://127.0.0.1:5000/evaluate in the URL field.
##### 4. Go to the "Body" tab, select "raw" and "JSON", then paste your JSON data:
```python

[
    {
        "answer_1": "The cat is on the mat.",
        "answer_2": "There is a cat on the mat.",
        "answer_3": "A cat is sitting on a mat.",
        "answer_4": "On the mat, there is a cat.",
        "question": "Where is the cat?",
        "student_answer": "A cat is on the mat."
    }
]

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Comming Soon](https://)