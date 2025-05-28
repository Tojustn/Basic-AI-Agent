import unittest
from flaskr import create_app
class TestRoutes(unittest.TestCase):
    def setUp(self): # Sets up a local server to run tests
        self.app = create_app()
        self.client = self.app.test_client()

    def test_chat_post(self):
        res = self.client.post("/chat", json={"message": "hi"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("response", res.get_json()) # Checks if response is in the json 


if __name__ == "__main__":
    unittest.main()
