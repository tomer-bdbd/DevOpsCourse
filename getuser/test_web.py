import unittest
from unittest.mock import patch
import getpass
from main import app


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        """Test that the index route returns 200 and contains username"""
        with patch("getpass.getuser", return_value="testuser"):
            response = self.app.get("/")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"testuser", response.data)

    def test_health_route(self):
        """Test that the health route returns JSON with username"""
        with patch("getpass.getuser", return_value="testuser"):
            response = self.app.get("/health")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"testuser", response.data)
            self.assertIn(b"healthy", response.data)


if __name__ == "__main__":
    unittest.main()
