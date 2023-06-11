import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pokemon_data.csv')

spawn_rate_less_than_5 = data[data['spawn_chance'] < 5]
print("Pokemons with spawn rate less than 5%:")
print(spawn_rate_less_than_5[['name', 'spawn_chance']])
print()

less_than_4_weaknesses = data[data['weakness_count'] < 4]
print("Pokemons with less than 4 weaknesses:")
print(less_than_4_weaknesses[['name', 'weakness_count']])
print()

no_multipliers = data[data['multiplier_count'] == 0]
print("Pokemons with no multipliers:")
print(no_multipliers[['name', 'multiplier_count']])
print()

less_than_2_evolutions = data[data['evolution_count'] <= 2]
print("Pokemons with less than or equal to 2 evolutions:")
print(less_than_2_evolutions[['name', 'evolution_count']])
print()

data['spawn_time'] = pd.to_datetime(data['spawn_time'], format='%M:%S')
spawn_time_less_than_300 = data[data['spawn_time'].dt.total_seconds() < 300]
print("Pokemons with spawn time less than 300 seconds:")
print(spawn_time_less_than_300[['name', 'spawn_time']])
print()

more_than_2_types = data[data['type_count'] > 2]
print("Pokemons with more than 2 types of capabilities:")
print(more_than_2_types[['name', 'type_count']])
print()


plt.figure(figsize=(8, 6))
plt.bar(spawn_rate_less_than_5['name'], spawn_rate_less_than_5['spawn_chance'])
plt.xlabel('Pokemons')
plt.ylabel('Spawn Rate')
plt.title('Pokemons with Spawn Rate Less than 5%')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(6, 6))
plt.pie(less_than_4_weaknesses['weakness_count'].value_counts(), labels=less_than_4_weaknesses['weakness_count'].unique())
plt.title('Pokemons with Less than 4 Weaknesses')
plt.show()

plt.figure(figsize=(6, 6))
plt.pie(less_than_2_evolutions['evolution_count'].value_counts(), labels=less_than_2_evolutions['evolution_count'].unique())
plt.title('Pokemons with Less than or Equal to 2 Evolutions')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(spawn_time_less_than_300['spawn_time'], spawn_time_less_than_300['name'])
plt.xlabel('Spawn Time')
plt.ylabel('Pokemons')
plt.title('Pokemons with Spawn Time Less than 300 seconds')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 6))
plt.bar(more_than_2_types['name'], more_than_2_types['type_count'])
plt.xlabel('Pokemons')
plt.ylabel('Number of Types')
plt.title('Pokemons with More than 2 Types of Capabilities')
plt.xticks(rotation=90)
plt.show()
