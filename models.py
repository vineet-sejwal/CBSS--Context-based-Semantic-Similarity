from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movie_Details(models.Model):

	name=models.TextField(max_length=100, blank=True, null=True,)
	
	genre=models.TextField(max_length=500, blank=True, null=True)
	
	certification=models.TextField(max_length=200, blank=True, null=True)
	
	director=models.TextField(max_length=50, blank=True, null=True)

	cast=models.TextField(max_length=2000, blank=True, null=True)

	theatre_release=models.TextField(max_length=50, blank=True, null=True)

	dvd_out=models.TextField(max_length=50, blank=True, null=True)

	rating=models.TextField(max_length=50, blank=True, null=True)

	abstract=models.TextField(max_length=3000, blank=True, null=True)

	about=models.TextField(max_length=150, blank=True, null=True)

	based_on=models.TextField(max_length=150, blank=True, null=True)

	sub_genre=models.TextField(max_length=400, blank=True, null=True)

	academy_actor=models.TextField(max_length=10, blank=True, null=True)

	academy_actress=models.TextField(max_length=10, blank=True, null=True)

	academy_director=models.TextField(max_length=10, blank=True, null=True)

	academy_picture=models.TextField(max_length=10, blank=True, null=True)

	academy_cinematographer=models.TextField(max_length=10, blank=True, null=True)

	academy_visual_effects=models.TextField(max_length=10, blank=True, null=True)

	academy_animated_movie=models.TextField(max_length=10, blank=True, null=True)

	movie_bafta=models.TextField(max_length=10, blank=True, null=True)

	movie_golden_globe=models.TextField(max_length=10, blank=True, null=True)

	movie_set_timeline=models.TextField(max_length=5000, blank=True, null=True)

	movie_sequel=models.TextField(max_length=10, blank=True, null=True)

	movie_prequel=models.TextField(max_length=10, blank=True, null=True)

	total_sentiments=models.FloatField(max_length=20, blank=True, null=True, default=0.0)

	total_reviews = models.IntegerField(blank=True, null=True, default=0)

	total_sentiments_story = models.FloatField(max_length=20,blank=True, null=True, default=0.0)

	total_sentiments_cinematography = models.FloatField(max_length=20,blank=True, null=True, default=0.0)

	total_sentiments_performance = models.FloatField(max_length=20,blank=True, null=True, default=0.0)

	total_sentiments_scenes = models.FloatField(max_length=20,blank=True, null=True, default=0.0)

	total_sentiments_awards = models.FloatField(max_length=20,blank=True, null=True, default=0.0)

	total_sentiments_direction = models.FloatField(max_length=20,blank=True, null=True, default=0.0)

	total_sentiments_music = models.FloatField(max_length=20,blank=True, null=True, default=0.0)

	total_sentiments_visual_effects = models.FloatField(max_length=20,blank=True, null=True, default=0.0)

	movie_topics_lda = models.TextField(max_length=5000, blank=True, null=True)

	movie_similarity = models.TextField(max_length=70000, blank=True, null=True)

	movie_similarity_new = models.TextField(max_length=70000, blank=True, null=True)

	movie_similarity_jaccard = models.TextField(max_length=70000, blank=True, null=True)

	movie_similarity_pearson_correlation = models.TextField(max_length=70000, blank=True, null=True)

	movie_similarity_comparision_papers = models.TextField(max_length=70000, blank=True, null=True)

	movie_similarity_without_lda = models.TextField(max_length=70000, blank=True, null=True)

	movie_similarity_comparision_papers_new = models.TextField(max_length=70000, blank=True, null=True)


	def __unicode__(self):
		return self.name
		
		

class Reviewer_Profile(models.Model):

	reviewer_name=models.TextField(max_length=50,null=True,blank=True)

	reviewer_id=models.TextField(max_length=50,null=True,blank=True)

	review_user=models.TextField(max_length=8000,null=True,blank=True)

	review_date=models.TextField(max_length=50,blank=True,null=True)

	review_help=models.TextField(max_length=75,blank=True,null=True)

	review_heading=models.TextField(max_length=150,blank=True,null=True)

	movie_name=models.ForeignKey(Movie_Details,blank=True,null=True)

	review_score=models.FloatField(max_length=10, blank=True, null=True)

	movie_ratings=models.TextField(max_length=5,blank=True,null=True)

	def __unicode__(self):

		return '%s %s' % (self.reviewer_name, self.movie_name)




			


