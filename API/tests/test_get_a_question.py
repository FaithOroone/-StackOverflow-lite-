import json
import unittest
from unittest import TestCase

from question.views import app

class GetaQuestionTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.request_data = {
            "question_id":"1",
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
