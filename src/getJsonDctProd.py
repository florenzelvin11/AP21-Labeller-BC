import json

# Load JSON data from a file
with open('data.json') as json_file:
    data = json.load(json_file)

# Perform actions on found items
prod = "3M42DG"

if data.get(prod):
    print("Found item:", data.get(prod))
else:
    print("Item not found.")
