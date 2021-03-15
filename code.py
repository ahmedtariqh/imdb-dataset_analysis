import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
# Loading data .
df = pd.read_csv('tmdb-movies.csv')
# clean unwanted columns:
clean = df.drop(['original_title','cast','homepage','director','imdb_id'],axis = 1)
clean.drop(['tagline','keywords','overview','budget_adj','production_companies','revenue_adj'],axis = 1 , inplace = True)
# drop rows with missing values
clean.dropna(inplace=True)
#drop rows with zeros
clean = clean.loc[clean['budget']!=0]
clean = clean.loc[clean['revenue']!=0]
clean = clean.loc[clean['runtime']!=0]
clean = clean.loc[clean['popularity']!=0]
clean = clean.loc[clean['vote_count']!=0]
clean = clean.loc[clean['release_year']!=0]
#histograms for all dataset features
clean.hist(figsize=(15,15))
#stats

#means
print("mean revenue is ",clean['revenue'].mean()," mean budget is " ,clean['budget'].mean() , "mean vote average is",clean['vote_average'].mean(),"mean runtime is",clean['runtime'].mean(),"mean release year is",clean['release_year'].mean())
#old and new movies
old = clean[clean['release_year'] < 2001]
new = clean[clean['release_year'] >= 2001]
#high and low budgets
high_budget = clean[clean['budget']>= 37201828.2915]
low_budget = clean[clean['budget']< 37201828.2915]
print('mean popularity in old movies is',old['popularity'].mean(),"while in new ones is",new['popularity'].mean())
#old and new according to revenue
fig ,ax = plt.subplots(figsize=(6,6))
ax.hist(old['revenue'],alpha = 0.5,label = 'Old Movies')
ax.hist(new['revenue'],alpha = 0.5,label = 'New Movies')
ax.set_xlabel('Revenue')
ax.set_ylabel('Count')
ax.set_title('Revenue according to date of release')
ax.legend(loc='upper right')
plt.show()
#generally new movies generated more revenue
#highest budgets and lowest budgets according to vote average
fig ,ax = plt.subplots(figsize=(8,6))
ax.hist(high_budget['vote_average'],alpha = 0.5,label = 'Highest Budget Movies')
ax.hist(low_budget['vote_average'],alpha = 0.5,label = 'Lowest Budget Movies')
ax.set_xlabel('Vote Average')
ax.set_ylabel('Count')
ax.set_title('Votes according to budgets')
ax.legend(loc='upper right')
plt.show()
#assuring result:
#clean.plot.scatter(x='budget',y='vote_average')
print(high_budget['vote_average'].max() ,",",
low_budget['vote_average'].max())
#how many movies were made in each year
ax =clean['release_year'].value_counts().plot(kind='bar',legend=True,title='Movies Per Year',figsize=(13,10))
ax.set_xlabel("Year")
ax.set_ylabel("Number of movies")
#scatter plot budget against revenue
clean.plot.scatter(x='budget',y='revenue').set_title('Relation between budget and revenue')
#plotting budget against popularity in the whole dataset
clean.plot.scatter(x='budget',y='popularity').set_title('Relation between budget and popularity')
#how budget affects popularity in new and old movies
old.plot.scatter(x='budget',y='popularity').set_title('How budget affects popularity in old movies')
new.plot.scatter(x='budget',y='popularity').set_title('How budget affects popularity in new movies')
#relation between vote average and runtime
clean.plot.scatter(x='runtime',y='vote_average')
#relation between popularity and runtime
clean.plot.scatter(x='runtime',y='popularity')
#plotting popularity of the old and new dataset
fig ,ax = plt.subplots(figsize=(8,6))
ax.hist(old['popularity'],alpha = 0.5,label = 'Popularity of Old Movies')
ax.hist(new['popularity'],alpha = 0.5,label = 'Popularity of New Movies')
ax.set_xlabel('Popularity')
ax.set_ylabel('Count')
ax.legend(loc='upper right')
plt.show()
#count how many times each genre is mentioned
action= clean['genres'].str.count('Action').sum()
adventure = clean['genres'].str.count('Adventure').sum()
scifi = clean['genres'].str.count('Science Fiction').sum()
thriller = clean['genres'].str.count('Thriller').sum()
fantasy = clean['genres'].str.count('Fantasy').sum()
crime = clean['genres'].str.count('Crime').sum()
drama = clean['genres'].str.count('Drama').sum()
western = clean['genres'].str.count('Western').sum()
family = clean['genres'].str.count('Family').sum()
animation = clean['genres'].str.count('Animation').sum()
romance = clean['genres'].str.count('Romance').sum()
music = clean['genres'].str.count('Music').sum()
history = clean['genres'].str.count('History').sum()
documentary = clean['genres'].str.count('Documentary').sum()
comedy = clean['genres'].str.count('Comedy').sum()
#create array of genres and another one for their labels
genres = [action,adventure,scifi,thriller,fantasy,crime,drama,western,family,animation,romance,music,history,documentary,comedy]
pie_labels = ['action','adventure','scifi','thriller','fantasy','crime','drama','western','family','animation','romance','music','history','documentary','comedy']
#bar chart of the main genres
fig = plt.figure(figsize=(12,4))
ax = fig.add_axes([0,0,1,1])
ax.bar(pie_labels,genres)
ax.set_xlabel('Genre')
ax.set_ylabel('Occurence')
plt.title('Most Popular Genres')
plt.show()
