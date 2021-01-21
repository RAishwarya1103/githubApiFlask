import unittest

import repos.api

class TestCreateQuery(unittest.TestCase):

    def test_create_query(self):
        test_languages=["Python","Ruby","Java"]
        test_min_stars=10000

        expected = "language:Python language:Ruby language:Java stars:>10000"
        result = repos.api.create_query(test_languages,test_min_stars)

        self.assertEqual(result, expected, "Unexpected results from create_query")

if __name__=='__main__':
    unittest.main()
