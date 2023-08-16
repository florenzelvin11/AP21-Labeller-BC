import json

# Load JSON data from a file
with open('data_dct.json') as json_file:
    data = json.load(json_file)

# Perform actions on found items
sku_barcode = "9349281000202"

if data.get(sku_barcode):
    print("Found item:", data.get(sku_barcode))
else:
    print("Item not found.")
