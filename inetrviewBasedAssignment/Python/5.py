import requests
import json
import re

def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def extract_data(data):
    show_id = data['id']
    show_url = data['url']
    show_name = data['name']
    episodes = data['_embedded']['episodes']

    extracted_data = []

    for episode in episodes:
        episode_data = {
            'season': episode['season'],
            'number': episode['number'],
            'type': episode['type'],
            'airdate': episode['airdate'],
            'airtime': episode['airtime'],
            'runtime': episode['runtime'],
            'average_rating': episode['rating']['average'],
            'summary': remove_html_tags(episode['summary']),
            'medium_image_link': episode['image']['medium'],
            'original_image_link': episode['image']['original']
        }
        extracted_data.append(episode_data)

    return show_id, show_url, show_name, extracted_data

def remove_html_tags(text):
    clean_text = re.sub('<.*?>', '', text)
    return clean_text

url = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'
downloaded_data = download_data(url)

show_id, show_url, show_name, extracted_data = extract_data(downloaded_data)

print("Show ID:", show_id)
print("Show URL:", show_url)
print("Show Name:", show_name)
print("Episode Data:")
for episode in extracted_data:
    print("- Season:", episode['season'])
    print("  Episode Number:", episode['number'])
    print("  Type:", episode['type'])
    print("  Airdate:", episode['airdate'])
    print("  Airtime:", episode['airtime'])
    print("  Runtime:", episode['runtime'])
    print("  Average Rating:", episode['average_rating'])
    print("  Summary:", episode['summary'])
    print("  Medium Image Link:", episode['medium_image_link'])
    print("  Original Image Link:", episode['original_image_link'])
    print("")
