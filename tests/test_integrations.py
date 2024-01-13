# tests/test_integration.py
import unittest
from app import app

class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_item_lifecycle(self):
       
        self.app.post('/add', data=dict(item='Integration Test'), follow_redirects=True)
       
        self.app.post('/update/0', data=dict(new_item='Updated Integration Test'), follow_redirects=True)
 
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
