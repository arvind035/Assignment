import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_json('http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes')

season_ratings = data['season'].value_counts().sort_index()

plt.figure(figsize=(8, 6))
plt.bar(season_ratings.index, season_ratings.values)
plt.xlabel('Season')
plt.ylabel('Number of Episodes')
plt.title('Number of Episodes per Season')
plt.show()

high_rating_episodes = data[data['rating'] > 8]
print("Episode Names with Average Ratings More than 8 for Each Season:")
print(high_rating_episodes[['season', 'name']])
print()

before_may_2019 = data[data['airdate'] < '2019-05']
print("Episode Names Aired Before May 2019:")
print(before_may_2019[['name', 'airdate']])
print()

highest_rating_episodes = data.groupby('season')['rating'].idxmax()
lowest_rating_episodes = data.groupby('season')['rating'].idxmin()
highest_ratings = data.loc[highest_rating_episodes][['season', 'name', 'rating']]
lowest_ratings = data.loc[lowest_rating_episodes][['season', 'name', 'rating']]
print("Episode Name with the Highest Rating for Each Season:")
print(highest_ratings)
print()
print("Episode Name with the Lowest Rating for Each Season:")
print(lowest_ratings)
print()

most_popular_episodes = data.groupby('season')['rating'].idxmax()
most_popular_summaries = data.loc[most_popular_episodes][['season', 'name', 'summary']]
print("Summary for the Most Popular Episode in Every Season:")
print(most_popular_summaries)
