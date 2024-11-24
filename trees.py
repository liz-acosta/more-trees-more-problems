import json
import pandas as pd

DUBLIN_TREES = "data/dublin_trees.json"
PROPERTY_DATA = "data/dublin-property.csv"

def extract_street_names(tree_data):
    streets = []

    for key, value in tree_data.items():
        # print("STREETS: ", streets)
        
        # print("KEY: ", key)
        # print("VALUE: ", value)

        if isinstance(value, dict):
            # print("IS INSTANCE")
            streets.extend(extract_street_names(value))
        
        elif isinstance(value, (int, float)):
            # print("THE VALUE IS ", value)
            # print("THE KEY IS ", key)
            if value > 0:
                # print("YES")
                # print("ADDING KEY: ", key)
                streets.append(key)
    
    return streets
 
def preprocess_tree_data(data_filepath):

    tree_data = json.load(open(data_filepath))

    processed_data = {}
    
    for key, value in tree_data.items():
        # print("KEY: ", key)
        streets = extract_street_names(tree_data[key])
        # print("STREETS: ", streets)
        processed_data[key] = streets
    
    return processed_data

def preprocess_property_data(data_filepath):
    
    property_data = pd.read_csv(data_filepath)

    property_data["Price"] = property_data["Price"].str.replace('€', '', regex=True).replace(',', '', regex=True).astype(float)

    print("PRICES: ", property_data["Price"])
    
    return property_data

def calculate_average_prices(preprocessed_property_data, processed_tree_data):
    
    results = {}
    
    for category, streets in processed_tree_data.items():
        print("CATEGORY: ", category)
        print("STREETS: ", streets)
        filtered = preprocessed_property_data[preprocessed_property_data["Street Name"].isin(streets)]
        print("FILTERED: ", filtered)
        print("NUMBER OF FILTERED: ", len(filtered))
        
        average_price = filtered["Price"].mean().round(2)

        print("AVERAGE PRICE: ", average_price)
        
        results[category] = average_price
    
    return results

def main():

    print("Calcuating the average cost of properties according to tree height ... ")

    preprocessed_tree_data = preprocess_tree_data(DUBLIN_TREES)

    preprocessed_property_data = preprocess_property_data(PROPERTY_DATA)

    calculated_averages = calculate_average_prices(preprocessed_property_data, preprocessed_tree_data)

    print(f"Average price of properties on streets with tall trees: €{calculated_averages['tall']}")
    print(f"Average price of properties on streets with short trees: €{calculated_averages['short']}")

# Run the script
if __name__ == "__main__":
    main()