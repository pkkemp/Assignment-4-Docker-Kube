from app import app
import unittest 

class FlaskBookshelfTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    def test_spell_check(self):
        # sends HTTP GET request to the application
        # on the specified path
        response = self.app.get('/spell_check', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        # sends HTTP GET request to the application
        # on the specified path
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/login', data=dict(uname='pw', pword='pw', twofact='123'))
        self.assertEqual(response.status_code, 200)
