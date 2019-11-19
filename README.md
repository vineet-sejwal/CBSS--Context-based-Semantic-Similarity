The python snippets given here extract the data from different sources and find similarity between movies using the extracted
features. Based-on the movie similarity, finally we predict the ratings for unrated movies. The whole program is written in Django framework, which can be downloaded from, https://www.djangoproject.com/. To store the data, we have used MySQL database. Django uses Object-relational mapping (ORM) concept which provides an easy query and database setup.



# CBSS--Context-based-Semantic-Similarity
CBSS -- A context-based semantic similarity computes the similarity between movies using contextual features extracted 
from movie data sources (IMDB and Rotten Tomatoes) and DBpedia (LOD). We are sharing 5 files which includes data extraction to 
rating prediction. Below i am providing a small description of each python file.

## Data_Crawler.py
This python program extracted the data from movie data sources. You need to provide the URL of the movie for which you want to extract the features. The python libraries such as beautiful soup and urllib are used to load the HTML file of each page. The basic information of movie such as genre, cast, director, and abstract are extracted from one movie data source, whereas reviews and ratings are extracted from another movie data source.

## DBpedia_Data.py
This python program extracts the contextual features of movies from DBpedia (nucleus of LOD). You need to provide the URI of movie
and this program returns <property, value> pair. We have extracted the subjective information; you need to change the property name for new features.

## Context-based_Similarity.py
This program computes the similarity score between movies using the extracted contextual features. For each matched feature, we first compute its completeness score in the dataset and then assign a weight. An iterative process is applied on the matched items with assigned weights to compute the similarity score.

## Rating_Prediction.py
This program predicts the rating for unrated item using the similarity score of items. We have used first order approximation to handle user and item biasness.

To predict the ratings for unrated items using CBSS, first you need to create a new project using DJANGO framework. The models file is used to create a table and fields in MYSQL DB. After that, to crawl the data, use Data_Crawler.py and DBpedia_Data.py files. Once the data is crawled, Context-based_similarity.py computes the similarity between items (movies) using the extracted contextual features. At last, Rating_Prediction.py predicts the ratings for unrated items.
