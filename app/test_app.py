import unittest
from app import app
import uuid

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_home(self):
        # sends HTTP GET request to the application
        # on the specified path
        response = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(response.status_code, 200)

        # assert the response data
        self.assertEqual(response.data.decode(), "Healthy")

    def test_new_uuid(self):
        response = self.app.get('/uuid')

        self.assertEqual(response.status_code, 200)

        # Check if the response is a valid UUID
        try:
            uuid_obj = uuid.UUID(response.data.decode(), version=4)
            is_valid_uuid = uuid_obj.hex == response.data.decode().replace('-', '')
        except ValueError:
            is_valid_uuid = False

        self.assertTrue(is_valid_uuid)

if __name__ == '__main__':
    unittest.main()
