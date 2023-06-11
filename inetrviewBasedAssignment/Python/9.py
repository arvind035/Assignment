import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD')

not_qualify_cars = data[data['Qualifies for Clean Alternative Fuel Vehicle?'] == 'No']
print("Cars and Types that do not qualify for clean alternative fuel vehicle:")
print(not_qualify_cars[['Make', 'Type']])
print()

tesla_cars = data[(data['Make'] == 'TESLA') & (data['City'] == 'BOTHELL')]
print("TESLA cars with model year and model type made in Bothell City:")
print(tesla_cars[['Model Year', 'Model Type']])
print()

electric_cars = data[(data['Electric Range'] > 100) & (data['Model Year'] > 2015)]
print("Cars with electric range more than 100 and made after 2015:")
print(electric_cars[['Make', 'Model Year', 'Electric Range']])
print()

city_ev_type_distribution = data.groupby(['City', 'Electric Vehicle Type']).size().unstack()
city_ev_type_distribution.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel('City')
plt.ylabel('Count')
plt.title('Distribution of Electric Vehicle Types by City')
plt.legend(title='Electric Vehicle Type')
plt.show()
