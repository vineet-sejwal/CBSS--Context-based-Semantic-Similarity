	query_list = [] # Enter the user id for which you need to predict ratings

	movie_list_mae = [] # Enter the id of the movie 
	
	

	for mov in movie_list_mae:

		
		for q in query_list:

			
			#import pdb;pdb.set_trace()
			for rw in Reviewer_Profile.objects.filter(reviewer_id__icontains=q):

				if rw.movie_ratings:

					if rw.movie_name_id == mov:		

						

			
						list12=[]
						simt_dict={}
						user_movie=[]
						user_movie1=[]
						n22={}
						movie_id={}
						import ast
						import operator
						import itertools
						from itertools import islice
						for i in Movie_Details.objects.filter(id=mov):

							new_dict=(i.movie_similarity)
							
						simt_dict = dict(list(ast.literal_eval(new_dict)))

						sorted_x = sorted(simt_dict.items(), key=operator.itemgetter(1))

						sorted_dict = dict(sorted_x[]) # enter the value of k (KNN)
						print sorted_dict
					
						

						

						
						for i in Reviewer_Profile.objects.filter(reviewer_id__icontains=q):
							user_movie.append(i.movie_name_id)

						print user_movie	
						for k in Movie_Details.objects.all():
							for i in user_movie:
								if k.id==i:
									user_movie1.append(k.name)
									
						
						
						n22 = {k: sorted_dict[k] for k in sorted_dict.viewkeys() & set(user_movie1)}

						print n22

						for b in Movie_Details.objects.all():

							movie_id[b.name] = b.id

					
						flat_lis = dict((movie_id[key], value) for (key, value) in n22.items())

						for r in flat_lis:

							for s in Movie_Details.objects.filter(id=r):

								print s.name
								print ('\n')
						
						mu = 6.12 # overall average rating of movies in dataset
						user_rating_count = 0
						no_of_movie = 0
						for k in Reviewer_Profile.objects.filter(reviewer_id__icontains=q):

							if k.movie_ratings:
								no_of_movie = no_of_movie +1
								user_rating_count = user_rating_count + int(k.movie_ratings[:-3])

						bu = float(user_rating_count)/no_of_movie
								
						if (mu>bu):   # user biasness
							bu = mu - bu
							bu=bu*(-1)
						if (mu<bu):
							bu=bu-mu	

						movie_rat = 0
						count_movie = 0	
						for r in Movie_Details.objects.filter(id=mov):
							
							bi = float(r.rating[:-3])	
						
						if (mu>bi):   # item biasness
							bi = mu - bi
							bi=bi*(-1)
						if (mu<bi):
							bi=bi-mu		


						total_similarity=0
						count_loop = 0
						sim_value = 0
						if flat_lis:
							for key, value in flat_lis.iteritems():
							
							
								for k in Reviewer_Profile.objects.filter(reviewer_id__icontains=q):

									if k.movie_ratings:

										if (key == k.movie_name_id):

											count_loop=count_loop+1

											sim_value = sim_value + value
											
											for bn in Movie_Details.objects.filter(id=key):
												bj = float(bn.rating[:-3])
											if (mu>bj):
												bj = mu - bj
												bj=bj*(-1)
											if (mu<bj):
												bj=bj-mu
											
											total_similarity = total_similarity + (float(k.movie_ratings[:-3]) - (mu + bj + bu)) * float ((value-0.5)/0.5)
						else:
							count_loop = 1

						if sim_value==0:	
							similarity_score = float(total_similarity)/1
						else:
							similarity_score = float(total_similarity)/sim_value	

						print rw.reviewer_name.encode('utf-8')

						f=open() # save the rating prediction value

						f.write(rw.reviewer_name.encode('utf-8'))

						f.write('\t')

						f.write(rw.movie_ratings[:-3])

						f.write('\t')

						differ = float(int(rw.movie_ratings[:-3]) - (mu + bi + bu + similarity_score))

						f.write(str(differ))

						print differ

						print mov

						f.write('\n')

						f.close()			
