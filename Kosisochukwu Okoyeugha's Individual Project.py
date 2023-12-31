#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


#read the csv file
netflix = pd.read_csv('netflix_data.csv')
print(netflix)


# In[7]:


#select a subset of column release year and duration
year_duration = netflix[['release_year', 'duration']]
print(year_duration)


# In[9]:


#select the range of rows with release year between 2011 and 2020
movie_dict = year_duration[(year_duration["release_year"] > 2010) & (year_duration["release_year"] < 2021)]
print(movie_dict)


# In[10]:


#calculate the mean of the duration grouped by release year
durations_df = movie_dict.groupby(["release_year"]).mean('duration')
print(durations_df)


# In[11]:


type(durations_df)


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


plt.plot(durations_df["release_year"], durations_df["duration"], marker = '0')
plt.xlabel('release_year')
plt.ylabel('duration')
plt.title('Netflix Movie Durations 2011-2020')
plt.show()


# In[21]:


netflix.df = pd.read_csv('netflix_data.csv')
netflix.df.head()


# In[22]:


#Subset the netflix_df DataFrame such that only rows where the type is a "Movie" are preserved. Assign the result to netflix_df_movies_only.
netflix_df_movies_only = netflix.df[netflix.df["type"] == "Movie"]
print(netflix_df_movies_only)


# In[23]:


# Subset the netflix_df_movies_only DataFrame to preserve only the columns title, country, genre, release_year, and duration. Assign the result to netflix_movies_col_subset
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]


# In[24]:


#Print the first five rows of netflix_movies_col_subset.
netflix_movies_col_subset.head()


# In[25]:


#Using your netflix_movies_col_subset DataFrame, create a scatter plot, placing the release_year on the x-axis and the movie duration on the y-axis
netflix_movies_col_subset.plot.scatter(x="release_year", y="duration")
#Add a title to your plot: "Movie Duration by Year of Release"
plt.title("Movie Duration by Year of Release", fontweight = 'bold')
#Show the plot
plt.show


# In[26]:


#Subset netflix_movies_col_subset to create a new DataFrame short_movies containing only movies that have a duration fewer than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]


# In[27]:


#Print the first 20 rows of short_movies to get a good overview of the types of films with a short duration
short_movies.head(20)


# In[28]:


# Initialize an empty list called colors to store our different color values
colors = []


# In[37]:


#Use a for loop to iterate through the netflix_movies_col_subset DataFrame's rows and append colors to your colors list based on the following conditions:
#If the genre is "Children", append "red"
#If the genre is "Documentaries", append "blue"
#If the genre is "Stand-Up", append "green"
#If the genre is any other genre, append "black".
colors = []
for index, row in netflix_movies_col_subset.iterrows():
    genre = row['genre']
    if genre =="Children":
        colors.append('red')
    elif genre == "Documentaries" :
        colors.append('blue')
    elif genre == "Stand-Up" :
        colors.append('green')  
    else:
        colors.append('black')


# In[38]:


# Print the first 10 values of your colors list to inspect the results
print(colors[:10])


# In[39]:


#Using the data contained in netflix_movies_col_subset, plot the same scatter plot as you did in Task 6, but with a few modifications:
#Color the points on the scatter plot using your colors list you defined in the previous step
#Add a title "Movie duration by year of release", an x-axis label "Release year", and a y-axis label "Duration (min)"
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c = colors)
plt.title("Movie duration by year of release", fontweight = 'bold')
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
#Show the plot.
plt.show


# In[4]:


#Provide your answer to the question "Are we certain that movies are getting shorter?" in the form of a string.
print("NO, movies are not getting shorter as fluctuation exists in movie duration between years")


# In[ ]:




