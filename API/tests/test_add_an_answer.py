import json
import unittest
from unittest import TestCase

from question.views import app


class PostanAnswerTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.request_data = {
            "answer_id"
            "question_id":1,
            "answer":"answer",
            "answered_by":"Faith"
        }
#post a question
    def test_post_an_answer(self):
        response = self.app.post('/api/v1/questions/<question_id>/answers', data = json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        #self.assertIn("you have posted your first question", str(response.data))

    if __name__ == '__main__':
        unittest.main
