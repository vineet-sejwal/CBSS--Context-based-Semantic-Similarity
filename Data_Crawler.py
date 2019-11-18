from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json
import re
from django.conf.urls import url
from django.db.models import Prefetch
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import urllib2, urllib
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError



# This program crawl the the information of movies from Rotten Tomatoes site. If you want to crawl some other data,
# then you need to enter the html tags.

	print "Please provide the movie name"
 
	raw=raw_input()
 
	url="https://www.rottentomatoes.com/m/"

	url=url[:33] +str(raw) + url[33:]
	
	page=urllib2.urlopen(url)

	soup=BeautifulSoup(page)
	
	# to print movie title

	for titl in soup.findAll('div',{"class":"col-sm-17 col-xs-24 score-panel-wrap"}):

		for title in titl.findAll('h1'):

			movie_title = (titl.get_text())


	
# to print genre of the movie
	movie_genre=''

	movie_genre = soup.findAll("div",{'class':'meta-value'})[1].get_text()
	movie_genre=movie_genre.strip()
	movie_genre=movie_genre.replace('\n', '')
	movie_genre=" ".join(movie_genre.split())


# to print the certification of the movie

	movie_certification=soup.findAll("div",{'class':'meta-value'})[0].get_text()


# to print the director

	mve_dirct = soup.findAll("div",{'class':'meta-value'})[2].get_text()

	mve_dirct=mve_dirct.strip()
	mve_dirct=mve_dirct.replace('\n', '')

	'''
# to print the rating of the movie
	rating= soup.findAll('li')#,{"class":"score-modal__details-wrap"})#[0].get_text()
	import pdb;pdb.set_trace()
	ratings= rating[50:]
	ratings=ratings.strip()
	'''
# to print the director and starcast

	movie_cast=''
	for i in soup.findAll('div',{"class":"castSection"}): # for cast

		for j in i.findAll('a'):
		
			movie_cast=movie_cast+","+(j.get_text()) 
			movie_cast=movie_cast.strip()
			movie_cast=movie_cast.replace('\n', '')
	

		movie_cast=" ".join(movie_cast.split())
	
# to print theatre release

	theatr = soup.findAll("div",{'class':'meta-value'})[4].get_text().replace('\n', '')
	#import pdb;pdb.set_trace()
	s=theatr.replace(',', '')
	s=s.strip()
	
	if (len(s)==16):

		s=s[:11]
		s=time.strptime(s,'%b %d %Y')
		movie_theater=time.strftime("%Y-%m-%d",s)

	elif (len(s)==15):
		s=s[:10]
		s=time.strptime(s,'%b %d %Y') 
		movie_theater=time.strftime("%Y-%m-%d",s) 
	   
	else:

		s=s[:10]
		s=time.strptime(s,'%b %d %Y')
		movie_theater=time.strftime("%Y-%m-%d",s)
	
# to print dvd out date
	
	cell= soup.findAll("div",{'class':'meta-value'})[5]
	s = cell.get_text().replace('\n', '')
	s=s.replace(',', '')
	s=s.strip()
	s=time.strptime(s,'%b %d %Y')
	cells=time.strftime("%Y-%m-%d",s)
	
	#cells='2013-05-12'



# to print the abstract of the movie

	for i in soup.findAll('div',{"class":"movie_synopsis clamp clamp-6"}):

		movie_synopsis = i.get_text() 
		movie_synopsis=movie_synopsis.strip()
		movie_synopsis= movie_synopsis.replace('\n', '')
	  

	for titl in soup.findAll('h1',{"class":"title clearfix visible-xs"}):

		movie_title = (titl.get_text()[17:])



	m=Movie_Details(name=movie_title,genre=movie_genre,certification=movie_certification,director=mve_dirct,rating=ratings,cast=movie_cast,theatre_release=movie_theater,dvd_out=cells,abstract=movie_synopsis)

	m.save()

	


# This program crawl the reviews and ratings of the reviwerer given on movies in IMDB site. If you want to crawl some other data,
# then you need to enter the html tags.
	
	
	
	rating_dict={}
	
	url =" " # Enter the URL of movie
		
	page=1
	while True:
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

		response = requests.get(url, headers=headers)

		soup=BeautifulSoup(response.content,'html.parser')
		
		for review in soup.find_all('div{"class:content"}): #HTML tags for reviews
		
			user_review = review.find('p').get_text()

		for k in soup.find_all('div',{"class":"review-container"}):  # HTML tags for ratings
			rating = k.find('span', class_='rating-other-user-rating')
			if rating:
				rating = ''.join(i.text for i in rating.find_all('span')[-2:])
			name = k.find('span', class_='display-name-link').a['href'][8:-12]
			#import pdb;pdb.set_trace()
			rating_dict[name]=rating

		load_more = soup.find('div', class_='load-more-data')
		if not load_more:
			break
		ajax_url ='/title/tt0114709/reviews/_ajax'

		url = 'http://www.imdb.com{}?paginationKey={}'.format(ajax_url, load_more['data-key'])
		time.sleep(3)
		print page
		page = page+1	
	
	m=Movie_Details(reviews = user_review, ratings = rating)

	m.save()

