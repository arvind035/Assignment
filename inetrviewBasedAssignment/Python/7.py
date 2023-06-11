import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('earth_meteorites.csv')

data['year'] = pd.to_datetime(data['year'], format='%Y')

before_2000 = data[data['year'].dt.year < 2000]
print("Earth meteorites fell before the year 2000:")
print(before_2000[['name', 'year']])
print()

before_1970 = data[data['year'].dt.year < 1970]
print("Earth meteorites fell before the year 1970 with coordinates:")
print(before_1970[['name', 'reclat', 'reclong']])
print()

mass_more_than_10000 = data[data['mass'] > 10000]
print("Earth meteorites with mass more than 10000 kg:")
print(mass_more_than_10000[['name', 'mass']])
print()


plt.figure(figsize=(8, 6))
plt.hist(before_2000['year'].dt.year, bins=20, edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Earth Meteorite Falls before the Year 2000')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(before_1970['reclong'], before_1970['reclat'], alpha=0.5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Earth Meteorite Falls before the Year 1970 (Coordinates)')
plt.show()

plt.figure(figsize=(8, 6))
plt.bar(mass_more_than_10000['name'], mass_more_than_10000['mass'])
plt.xlabel('Meteorites')
plt.ylabel('Mass (kg)')
plt.title('Earth Meteorites with Mass More than 10000 kg')
plt.xticks(rotation=90)
plt.show()