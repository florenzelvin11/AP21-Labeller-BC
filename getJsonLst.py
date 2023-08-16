import json

# Load JSON data from a file
with open('data_lst.json') as json_file:
    data = json.load(json_file)

# Create an index based on the search key
index = {}
search_key = "Prod"

for item in data:
    search_value = item.get(search_key)
    if search_value not in index:
        index[search_value] = []
    index[search_value].append(item)

# Search for items based on a specific value
search_value = "3M42DG"
found_items = index.get(search_value, [])

# Perform actions on found items
if found_items:
    for item in found_items:
        print("Found item:", item)
else:
    print("Item not found.")
