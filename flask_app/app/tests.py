import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_employee(self):
        response = self.app.post('/addemp', data=dict(emp_id='27', first_name='Erick', last_name='Cardiel', primary_skill='Python', location='Mexico'), follow_redirects=True)
        self.assertIn(b'Erick Cardiel', response.data)

    def test_get_employee(self):
        response = self.app.get('/getemp', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_fetch_data(self):
        response = self.app.post('/fetchdata', data=dict(emp_id='27'), follow_redirects=True)
        self.assertIn(b'Employee ID:', response.data)

if __name__ == "__main__":
    unittest.main()
