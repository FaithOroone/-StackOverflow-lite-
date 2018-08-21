import unittest
import json
from question.views import app
from unittest import TestCase

class GetaQuestionTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.request_data = {
            "question_id":"question_id",
            "username":"username",
            "question":"question"
        }

    def test_get_a_question(self):
        response = self.app.post('/api/v1/questions', data = json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.get('/api/v1/question/<int:question_id>', data = json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)

    if __name__ == '__main__':
        unittest.main