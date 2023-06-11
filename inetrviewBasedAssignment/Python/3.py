import requests
import json
import pandas as pd

def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def process_data(data):
    pokemon_list = []

    for pokemon in data['pokemon']:
        pokemon_data = {
            'id': pokemon['id'],
            'num': pokemon['num'],
            'name': pokemon['name'],
            'img': pokemon['img'],
            'type': ', '.join(pokemon['type']),
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'candy': pokemon.get('candy', ''),
            'candy_count': pokemon.get('candy_count', 0),
            'egg': pokemon['egg'],
            'spawn_chance': pokemon['spawn_chance'],
            'avg_spawns': pokemon['avg_spawns'],
            'spawn_time': pokemon['spawn_time'],
            'multipliers': ', '.join(map(str, pokemon.get('multipliers', []))),
            'weakness': ', '.join(pokemon['weaknesses']),
            'next_evolution': ', '.join([evolution['name'] for evolution in pokemon.get('next_evolution', [])]),
            'prev_evolution': ', '.join([evolution['name'] for evolution in pokemon.get('prev_evolution', [])])
        }
        pokemon_list.append(pokemon_data)

    return pokemon_list

def export_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel('pokemon_data.xlsx', index=False)

url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
downloaded_data = download_data(url)

processed_data = process_data(downloaded_data)

export_to_excel(processed_data)
print("Data exported to pokemon_data.xlsx file.")
