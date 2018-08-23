questions =[]

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



class Answer():
        def __init__(self, answer_id, question_id, answer, answered_by):
                self.answer_id=123456
                self.question_id=question_id
                self.answer= answer
                self.answered_by= answered_by

        def get_answer_id(self):
            return self.answer_id

        def get_question_id(self):
            return self.question_id

        def get_answer(self):
            return self.answer

        def get_answered_by(self):
            return self.answered_by
answers = []
