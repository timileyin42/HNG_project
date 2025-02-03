import unittest
from app import app, is_prime, is_perfect, is_armstrong

class TestNumberClassificationAPI(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    # Test helper functions
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))

    def test_is_perfect(self):
        self.assertTrue(is_perfect(6))
        self.assertTrue(is_perfect(28))
        self.assertFalse(is_perfect(5))
        self.assertFalse(is_perfect(10))

    def test_is_armstrong(self):
        self.assertTrue(is_armstrong(153))
        self.assertTrue(is_armstrong(371))
        self.assertFalse(is_armstrong(123))
        self.assertTrue(is_armstrong(9474))

    # Test API endpoint
    def test_classify_number_valid_input(self):
        response = self.app.get('/api/classify-number?number=371')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['number'], 371)
        self.assertEqual(data['is_prime'], False)
        self.assertEqual(data['is_perfect'], False)
        self.assertEqual(data['properties'], ['armstrong', 'odd'])
        self.assertEqual(data['digit_sum'], 11)
        self.assertIn("371 is a narcissistic number", data['fun_fact'])

    def test_classify_number_invalid_input(self):
        response = self.app.get('/api/classify-number?number=abc')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['number'], 'abc')
        self.assertEqual(data['error'], True)

    def test_classify_number_negative_input(self):
        response = self.app.get('/api/classify-number?number=-28')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['number'], -28)
        self.assertEqual(data['is_prime'], False)
        self.assertEqual(data['is_perfect'], False)
        self.assertEqual(data['properties'], ['even'])
        self.assertEqual(data['digit_sum'], 10)

    def test_classify_number_large_input(self):
        response = self.app.get('/api/classify-number?number=9474')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['number'], 9474)
        self.assertEqual(data['is_prime'], False)
        self.assertEqual(data['is_perfect'], False)
        self.assertEqual(data['properties'], ['armstrong', 'even'])
        self.assertEqual(data['digit_sum'], 24)

if __name__ == '__main__':
    unittest.main()
