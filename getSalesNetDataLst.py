import csv
import json
import requests

def csv_to_json(csv_url):
    try:
        # Initialize a dictionary to store the JSON data
        json_data = {}
        response = requests.get(csv_url)
        response.raise_for_status()

        csv_data = response.text
        csv_reader = csv.DictReader(csv_data.splitlines())
        
        json_data = json.dumps([row for row in csv_reader], indent=4)
        return json_data
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    csv_url = "https://salesnet.brandcollective.com.au/LabelBarcodes/LabelBarcodes.csv"
    json_data = csv_to_json(csv_url)

    if not json_data.startswith("An error occurred:"):
        with open("data_lst.json", "w") as json_file:
            json_file.write(json_data)
            print("CSV data converted and saved as data_lst.json")
    else:
        print(json_data)
