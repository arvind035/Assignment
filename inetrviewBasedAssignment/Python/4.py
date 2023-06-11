import requests
import json
import csv

def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def process_data(data):
    processed_data = []

    for meteorite in data:
        meteorite_data = {
            'name': meteorite['name'],
            'id': meteorite['id'],
            'nametype': meteorite['nametype'],
            'recclass': meteorite['recclass'],
            'mass': meteorite['mass (g)'],
            'year': meteorite['year'],
            'reclat': meteorite['reclat'],
            'reclong': meteorite['reclong'],
            'coordinates': [meteorite['reclat'], meteorite['reclong']]
        }
        processed_data.append(meteorite_data)

    return processed_data

def export_to_csv(data):
    keys = data[0].keys()
    with open('meteorite_data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

url = 'https://data.nasa.gov/resource/y77d-th95.json'
downloaded_data = download_data(url)

processed_data = process_data(downloaded_data)

export_to_csv(processed_data)
print("Data exported to meteorite_data.csv file.")