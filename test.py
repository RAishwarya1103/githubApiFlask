import unittest

import repos.api
import repos.exceptions

class TestCreateQuery(unittest.TestCase):

    def test_create_query(self):
        test_languages=["Python","Ruby","Java"]
        test_min_stars=10000

        expected = "language:Python language:Ruby language:Java stars:>10000"
        result = repos.api.create_query(test_languages,test_min_stars)

        self.assertEqual(result, expected, "Unexpected results from create_query")

    def test_error_403(self):
        test_status_code=403
        result=repos.exceptions.GitHubApiError(test_status_code)

        self.assertTrue("Rate limit" in str(result),"'Rate limit' not found")
    
    def test_error_500(self):
        test_status_code=500
        result=repos.exceptions.GitHubApiError(test_status_code)

        self.assertTrue(str(test_status_code) in str(result))
    

if __name__=='__main__':
    unittest.main()
