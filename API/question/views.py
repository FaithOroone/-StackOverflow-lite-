from flask import Flask, request, jsonify, make_response
from models import Question, questions

app = Flask(__name__)
#post a question
@app.route('/api/v1/questions', methods=['POST'])
def post_aquestion():
	request_data = request.get_json()

	username = str(request_data.get('username'))
	question = str(request_data.get('question'))
	question_id = len(questions) + 1

	if not request_data:
    		return jsonify({'message':'please ask a question'}),400

	if not username or username == type(int) or username == " " or len(username) < 3:
		return jsonify({'message':'name is required'}), 400

	if not question or question == type(int) or question == "" or len(question) < 3:
		return jsonify({'message':'question is required'}), 400

	questions.append(request_data)
	return jsonify({"message":questions}), 201


#get questions
@app.route('/api/v1/question', methods=["GET"])
def fetch_questions():
    if len(questions)>0:
        return jsonify({"message":questions}), 200
    #else:
        #return jsonify({"message":"There are no questions found"}),404

#fetch a specific question
@app.route('/api/v1/question/<int:question_id>', methods=['GET'])
def get_a_question(question_id):
    for question in questions:
        if question['question_id'] == question_id:
            question = {
				'question_id':question_id['question_id'],
                'username': question['username'],
                'question': question['question']
            }
    return jsonify({'message':question}), 200

