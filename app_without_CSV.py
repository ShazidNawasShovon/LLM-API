from flask import Flask, request, jsonify
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer, util
import time
import json
from datetime import datetime

app = Flask(__name__)

# Load the pre-trained model
model_name = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
sentence_model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

def get_similarity(reference_answers, student_answer):
    try:
        # Encode sentences to get their embeddings
        ref_embeddings = sentence_model.encode(reference_answers, convert_to_tensor=True)
        student_embedding = sentence_model.encode(student_answer, convert_to_tensor=True)

        # Compute cosine similarities
        cosine_scores = util.pytorch_cos_sim(student_embedding, ref_embeddings)

        # Calculate the average similarity score
        average_score = torch.mean(cosine_scores).item()
        return average_score
    
    except Exception as e:
        return None  # Return None in case of any error during similarity calculation

def get_mark(average_score):
    try:
        # Convert similarity score to a mark out of 5
        if average_score >= 0.9:
            return 5
        elif average_score >= 0.8:
            return 4
        elif average_score >= 0.7:
            return 3
        elif average_score >= 0.6:
            return 2
        elif average_score >= 0.5:
            return 1
        else:
            return 0
    
    except Exception as e:
        return 0  # Return 0 if there's an error in calculating the mark

def format_timestamp(timestamp):
    try:
        # Convert timestamp to datetime object
        dt_object = datetime.fromtimestamp(timestamp)
        
        # Format datetime object to desired format
        formatted_time = dt_object.strftime('%d/%m/%Y at %I:%M %p')  # Use '%I' for 12-hour format with leading zero
        
        return formatted_time
    
    except Exception as e:
        return "Error formatting timestamp"  # Return a default message if there's an error in formatting the timestamp

@app.route('/', methods=['GET'])
def home():
    try:
        data = {
            'page': 'Home',
            'message': 'Successfully created API client; Please use "/evaluate" to evaluate student answers',
            'timestamp': format_timestamp(time.time())
        }
        return jsonify(data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error response with status code 500 if an exception occurs

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.json
        
        if not data or not isinstance(data, list):
            return jsonify({'error': 'Invalid JSON data provided'}), 400
        
        df = pd.DataFrame(data)

        df['similarity_score'] = df.apply(lambda row: get_similarity([row['answer_1'], row['answer_2'], row['answer_3'], row['answer_4']], row['student_answer']), axis=1)
        df['mark'] = df['similarity_score'].apply(lambda x: get_mark(x) if x is not None else 0)

        response_data = {
            'page': 'Evaluate',
            'message': 'Successfully evaluated student answers',
            'timestamp': format_timestamp(time.time()),
            'results': df.to_dict(orient='records')
        }

        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error response with status code 500 if an exception occurs

if __name__ == '__main__':
    app.run(debug=True)
