class Question():
    def __init__(self, question_id, username, question):
        self.question_id = 0
        self.username = username
        self.question = question

    def get_question_id(self):
            return self.question_id

    def get_username(self):
            return self.username

    def get_question(self):
            return self.question

questions =[]

class Answer:
    def __init__(self, answer_id,question_id, answered_by,answer):
        self.answer_id= answer_id
        self.question_id = question_id
        self.answered_by = answered_by
        self.answer = answer

    def get_question_id(self):
        return self.question_id

    def get_answered_by(self):
        return self.answered_by

    def get_answer(self):
        return self.answer

answers =[]
