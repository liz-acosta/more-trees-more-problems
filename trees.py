import json

DUBLIN_TREES = "data/dublin_trees.json"

# returns JSON object as a dictionary
tree_data = json.load(open(DUBLIN_TREES))

def extract_street_names(tree_data):
    streets = []

    for key, value in tree_data.items():
        print("STREETS: ", streets)
        
        print("KEY: ", key)
        print("VALUE: ", value)

        if isinstance(value, dict):
            print("IS INSTANCE")
            streets.extend(extract_street_names(value))
        
        elif isinstance(value, (int, float)):
            print("THE VALUE IS ", value)
            print("THE KEY IS ", key)
            if value > 0:
                print("YES")
                print("ADDING KEY: ", key)
                streets.append(key)
    
    return streets