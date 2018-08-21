from flask import Flask, request, jsonify, make_response
from models import Question, questions
import re

app = Flask(__name__)
#post a question
@app.route('/api/v1/questions', methods=['POST'])
def post_aquestion():
	request_data = request.get_json()
	if not request_data:
		return jsonify({'message':'please ask a question'}), 400

	question_id = request_data.get('question_id')
	username = str(request_data.get('username'))
	question = str(request_data.get('question'))

	if not question_id or question_id == " ":
    		return jsonify({'message':'A valid question_id is required'}), 400

	if not username or username == type(int) or username == " " or len(username) < 3:
		return jsonify({'message':'name is required'}), 400

	if not question or question == type(int) or question == "" or len(question) < 3:
		return jsonify({'message':'question is required'}), 400

	questions.append(request_data)
	return jsonify({"message":"you have posted your first question"}), 201


#get questions
@app.route('/api/v1/question', methods=["GET"])
def fetch_questions():
    if len(questions)>0:
        return jsonify({"message":questions}), 302
    else:
        return jsonify({"message":"There are no questions found"}),404

#fetch a specific question
@app.route('/api/v1/question/<int:question_id>', methods=['GET'])
def get_a_question():
    question = {}
    for question in questions:
        if question['question_id'] == question_id:
            question = {
                'username': question['username'],
                'question': question['question']
            }
    return jsonify({'message':'you have fetched a question'}), 302

