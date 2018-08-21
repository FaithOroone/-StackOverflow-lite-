import unittest
import json
from question.views import app
from unittest import TestCase

class GetQuestionTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user_data = {
            "user_profile":"ghhdggg",
            "username":"kerenagemo",
            "question":"sasdfggjh"
        }
    def test_fetch_question(self):
        response = self.app.post('api/v1/user/question', data = json.dumps(self.user_data), content_type = 'application/json')
        response = self.app.get('api/v1/user/questions', data = json.dumps(self.user_data), content_type = 'application/json')
        self.assertEqual(response.status_code,404)

    if __name__ == '__main__':
        unittest.main