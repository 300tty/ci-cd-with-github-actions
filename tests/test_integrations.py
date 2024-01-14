import unittest
from app import app, items

class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        items.append('Integration Test')  # Set up initial state

    def tearDown(self):
        items.clear()  # Clean up after each test

    def test_add_and_verify_item(self):
        response = self.app.post('/add', data=dict(item='Another Test'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/')
        self.assertIn('Another Test', response.get_data(as_text=True))

    def test_update_item(self):
        response = self.app.post('/update/0', data=dict(new_item='Updated Test'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/')
        self.assertIn('Updated Test', response.get_data(as_text=True))

    def test_delete_item(self):
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/')
        self.assertNotIn('Integration Test', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
