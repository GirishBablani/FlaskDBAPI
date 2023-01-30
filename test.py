try:
    from api import app
    import unittest
except Exception as e:
    print(f"Some modules are missing {e}")


class Flasktest(unittest.TestCase):
    def test_index_code_getData(self):
        tester = app.test_client(self)
        response = tester.post("/tourist/data")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_index_content_getData(self):
        tester = app.test_client(self)
        response = tester.post("/tourist/data")
        statuscode = response.status_code
        self.assertEqual(response.content_type,"application/json")

    # def test_index_content_postData(self):
    #     tester = app.test_client(self)
    #     response = tester.post("/tourist/post")
    #     statuscode = response.status_code
    #     self.assertEqual(response.content_type,"application/json")        
    
    
    # def test_index_code_postData(self):
    #     tester = app.test_client(self)
    #     response = tester.post("/tourist/post")
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode,200)

    
    # def test_index_content_updateData(self):
    #     tester = app.test_client(self)
    #     response = tester.put("/tourist/post")
    #     statuscode = response.status_code
    #     self.assertEqual(response.content_type,"application/json")        
    
    
    # def test_index_code_updateData(self):
    #     tester = app.test_client(self)
    #     response = tester.put("/tourist/post")
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode,200)

    
    # def test_index_content_deleteData(self):
    #     tester = app.test_client(self)
    #     response = tester.delete("/tourist/post")
    #     statuscode = response.status_code
    #     self.assertEqual(response.content_type,"application/json")        
    
    
    # def test_index_code_deleteData(self):
    #     tester = app.test_client(self)
    #     response = tester.delete("/tourist/post")
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode,200)

    
    def test_index_content_searchData(self):
        tester = app.test_client(self)
        response = tester.post("/tourist/search")
        statuscode = response.status_code
        self.assertEqual(response.content_type,"application/json")        
    
    
    def test_index_code_searchData(self):
        tester = app.test_client(self)
        response = tester.post("/tourist/search")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)    


if __name__=="__main__":
    unittest.main()

