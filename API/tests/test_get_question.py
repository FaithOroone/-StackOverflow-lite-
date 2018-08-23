import json
import unittest
from unittest import TestCase

from question.views import app


class GetaQuestionTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.request_data = {
            "question_id":"question_id",
            "username":"kerenagemo",
            "question":"sasdfggjh"
        }
    def test_fetch_questions(self):
        response = self.app.post('/api/v1/questions', data = json.dumps(self.request_data), content_type = 'application/json')
        response = self.app.get('/api/v1/question', data = json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code,302)

    if __name__ == '__main__':
        unittest.main
