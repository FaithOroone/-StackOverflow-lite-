from flask import Flask, Response, request, jsonify, make_response
from models import Question, Answer, questions, answers


app = Flask(__name__)
#post a question
@app.route('/api/v1/questions', methods=['POST'])
def post_aquestion():
	request_data = request.get_json()
	if not request_data:
		return jsonify({'message':'please ask a question'}), 400

	question_id = Question.get_question_id
	username = str(request_data.get('username'))
	question = str(request_data.get('question'))

	if not question_id or question_id == " ":
    		return jsonify({'message':'A valid question_id is required'}), 400

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
        return jsonify({"message":questions}), 302
    else:
        return jsonify({"message":"There are no questions found"}),

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

#add an answer
@app.route('/api/v1/question/<question_id>/answer', methods=['POST'])
def add_an_answer(question_id):
    request_data= request.get_json()
    valid_qna=request.get('valid_qna')
    answer_id = len(answers)+ 1

    if (valid_qna(request_data)):
        qna ={
            'answer_id': answer_id,
            'question_id':request_data.get('question_id'),
            'answered_by':request_data.get('answered_by'),
            'answer':request_data.get('answer'),

        }
        answers.append(qna)
        response =Response("",201, mimetype="application/json")
        response.headers['Location']="answers/" + str(request_data['question_id'])
        return response


