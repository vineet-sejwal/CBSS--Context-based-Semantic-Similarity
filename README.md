The python snippets given here extract the data from different sources and find similarity between movies using the extracted
features. Based-on the movie similarity, finally we predict the ratings for unrated movies. The whole program is written in Django framework, which can be downloaded from:
https://www.djangoproject.com/


# CBSS--Context-based-Semantic-Similarity
CBSS -- A context-based semantic similarity computes the similarity between movies using contextual features extracted 
from movie data sources (IMDB and Rotten Tomatoes) and DBpedia (LOD). We are sharing 5 files which includes data extraction to 
rating prediction. Below i am providing a small description of each python file.

## Data_Crawler.py
This python program extracted the data from movie data sources. You need to provide the URL of the movie for which you want to extract the features. The python libraries such as beautiful soup and urllib are used to load the HTML file of each page. The basic information of movie such as genre, cast, director, and abstract are extracted from one movie data source, whereas reviews and ratings are extracted from another movie data source.

## DBpedia_Data.py
This python program extract the contextual features of movies from DBpedia (nucleus of LOD). You need to provide the URI of movie
and this program returns <property, value> pair. We have extracted the subjective information, you need to change the property name for new features.
