import json
import unittest
from trees import extract_street_names

DUBLIN_TREES = "tests/test_data/test_dublin_trees.json"
EXPECTED_DUBLIN_TREES = "tests/test_data/expected_test_dublin_trees.json"

class TestTrees(unittest.TestCase):
 
    def test_extract_street_names(self):
        
        test_tree_data = json.load(open(DUBLIN_TREES))["short"]
        test_results = extract_street_names(test_tree_data)

        print("TEST RESULTS: ", test_results)

        expected_test_results = json.load(open(EXPECTED_DUBLIN_TREES))

        print("EXPECTED TEST RESULTS: ", expected_test_results["short"])

        self.assertEqual(len(test_results), len(expected_test_results["short"]))
        self.assertCountEqual(test_results, expected_test_results["short"])
        
        