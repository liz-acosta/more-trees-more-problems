import json
import unittest
import pandas as pd
from trees import extract_street_names, preprocess_tree_data, preprocess_property_data, calculate_average_prices

DUBLIN_TREES = "tests/test_data/test_dublin_trees.json"
EXPECTED_DUBLIN_TREES = "tests/test_data/expected_test_dublin_trees.json"
EXPECTED_AVERAGE_COST = "tests/test_data/expected_average_cost.json"
TEST_DUBLIN_PROPERTY = "tests/test_data/test_dublin-property.csv"

class TestTrees(unittest.TestCase):
 
    def test_extract_street_names(self):
        
        test_tree_data = json.load(open(DUBLIN_TREES))["short"]
        test_results = extract_street_names(test_tree_data)

        print("TEST RESULTS: ", test_results)

        expected_test_results = json.load(open(EXPECTED_DUBLIN_TREES))

        print("EXPECTED TEST RESULTS: ", expected_test_results["short"])

        self.assertEqual(len(test_results), len(expected_test_results["short"]))
        self.assertCountEqual(test_results, expected_test_results["short"])

    def test_preprocess_tree_data(self):
        
        test_tree_data = json.load(open(DUBLIN_TREES))
        test_results = preprocess_tree_data(DUBLIN_TREES)

        print("TEST RESULTS: ", test_results)

        expected_test_results = json.load(open(EXPECTED_DUBLIN_TREES))

        print("EXPECTED TEST RESULTS: ", expected_test_results)

        self.assertCountEqual(test_results, expected_test_results)
        self.assertEqual(list(test_results.keys()), ["short", "tall"])
        self.assertEqual(test_results["short"], expected_test_results["short"])
        self.assertEqual(test_results["tall"], expected_test_results["tall"])
    
    def test_preprocess_property_data(self):
        
        test_dublin_property = pd.read_csv(TEST_DUBLIN_PROPERTY)
        
        test_results = preprocess_property_data(TEST_DUBLIN_PROPERTY)

        print("TEST RESULTS: ", test_results)

        expected_test_results = json.load(open(EXPECTED_AVERAGE_COST))

        print("EXPECTED TEST RESULTS: ", expected_test_results)

        self.assertTrue(pd.api.types.is_float_dtype(test_results["Price"]))
     
    def test_calculate_average_prices(self):
        
        test_preproccessed_data = json.load(open(EXPECTED_DUBLIN_TREES))
        expected_test_results = json.load(open(EXPECTED_AVERAGE_COST))
        test_dublin_property = preprocess_property_data(TEST_DUBLIN_PROPERTY)
        
        test_results = calculate_average_prices(test_dublin_property, test_preproccessed_data)

        print("TEST RESULTS: ", test_results)

        expected_test_results = json.load(open(EXPECTED_AVERAGE_COST))

        print("EXPECTED TEST RESULTS: ", expected_test_results)

        self.assertEqual(test_results, expected_test_results)             