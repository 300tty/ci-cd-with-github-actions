import unittest
from app import app

class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_and_verify_item(self):
        self.app.post('/add', data=dict(item='Integration Test'), follow_redirects=True)
        response = self.app.get('/')
        self.assertIn(b'Integration Test', response.data)

    def test_update_item(self):
        self.app.post('/add', data=dict(item='Integration Test'), follow_redirects=True)
        self.app.post('/update/0', data=dict(new_item='Updated Test'), follow_redirects=True)
        response = self.app.get('/')
        self.assertIn(b'Updated Test', response.data)

    def test_delete_item(self):
        self.app.post('/add', data=dict(item='Integration Test'), follow_redirects=True)
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/')
        self.assertNotIn(b'Integration Test', response.data)

if __name__ == '__main__':
    unittest.main()

