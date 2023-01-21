try:
    from api import app
    import unittest
except Exception as e:
    print(f"Some modules are missing {e}")


class Flasktest(unittest.TestCase):
    def test_index_code(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(response.content_type,"application/json")    

if __name__=="__main__":
    unittest.main()

