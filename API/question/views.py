from flask import Flask, Response, request, jsonify, make_response
from models import Question, Answer, answers, questions

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

@app.route('/api/v1/questions/<question_id>/answers', methods =['POST'])
def add_an_answer():
	request_data = request.get_json()
	answer_id = len(answers) + 1
	question_id = request_data.get('question_id')
	answered_by = request_data.get('answered_by')
	answer = str(request_data.get('answer'))

	if not request_data:
    		return jsonify({'message':'please add your question'}),400

	if request_data:

        	answers.append(request_data)
        response =Response("",201, mimetype="application/json")
        response.headers['Location']="answers/" + str(request_data['question_id'])
        return response


