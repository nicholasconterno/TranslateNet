import unittest
import s2s_model  # Assuming this is your Flask app module


class BasicTests(unittest.TestCase):

    def setUp(self):
        # Set up your Flask test client
        self.app = s2s_model.app.test_client()
        self.app.testing = True

    def test_main_page(self):
        # Testing the local instance, not the live server
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
