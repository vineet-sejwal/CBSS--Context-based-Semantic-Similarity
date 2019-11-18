# This program computes the similarity between movies using the contextual features

def contextbasedsimilarity(request):

	feature_dict={}	

	movie_list = [] # enter the movie id for which similarity need to be computed

	

	for moviename in movie_list:

		for i in Movie_Details.objects.filter(id=moviename):
			m1_string = i.genre
			m1_genre = m1_string.split(',')

			y1_string = i.sub_genre
			m1_sub_genre = y1_string.split(',')

			d1_string = i.director.encode('utf-8')
			m1_director = d1_string.split(',')

			ca1_string = i.cast.encode('utf-8')
			m1_cast = ca1_string.split(',')


			based_on1_string = i.based_on
			m1_based_on = based_on1_string.split(',')

			about1_string = i.about
			m1_about = about1_string.split(',')

			movie_topics_lda_string1 = str(i.movie_topics_lda)
			movie_topics_lda1 = movie_topics_lda_string1.split(', ')		

			rating1 = i.rating[:3]

			theatre1 = i.theatre_release[:4]



			for k in Movie_Details.objects.all():
				m2_string = k.genre
				m2_genre = m2_string.split(',')

				y2_string = k.sub_genre
				m2_sub_genre = y2_string.split(',')

				d2_string = k.director.encode('utf-8')
				m2_director = d2_string.split(',')

				ca2_string = k.cast.encode('utf-8')
				m2_cast = ca2_string.split(',')

				based_on2_string = k.based_on
				m2_based_on = based_on2_string.split(',')

				about2_string = k.about
				m2_about = 	about2_string.split(',')

				movie_topics_lda_string2 = str(k.movie_topics_lda)
				movie_topics_lda2 = movie_topics_lda_string2.split(', ')	
				
				rating2 = k.rating[:3]

				theatre2 = k.theatre_release[:4]
				
				genre1 = Counter(m1_genre)
				genre2 = Counter(m2_genre)

				sub_genre1=Counter(m1_sub_genre)
				sub_genre2=Counter(m2_sub_genre)

				director1 = Counter(m1_director)
				director2 = Counter(m2_director)

				
				cast1 = Counter(m1_cast)
				cast2 = Counter(m2_cast)

				based_on1 = Counter(m1_based_on)
				based_on2 = Counter(m2_based_on)

				about1 = Counter(m1_about)
				about2 = Counter(m2_about)

				movie_topic1=Counter(movie_topics_lda1)
				movie_topic2=Counter(movie_topics_lda2)
				

				b3 = [val for val in genre1 if val in genre2]
				b4 = [val for val in sub_genre1 if val in sub_genre2]
				b5 = [val for val in director1 if val in director2]
				b6 = [val for val in cast1 if val in cast2]
				b7 = [val for val in based_on1 if val in based_on2]
				b8 = [val for val in about1 if val in about2]
				b10 = [val for val in movie_topic1 if val in movie_topic2]
				
				b9 = len(b3) + len(b4) + len(b5) + len(b7) + len(b8) + len(b10)
			
				rating_sum = (10 - abs(float(rating1)-float(rating2)))/10

				if (b3):

					genre=0
					for element in b3:
						
						element_count=0
						for movie in Movie_Details.objects.all():
							
							movie_genre11=movie.genre.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							
						
						prob=1-(element_count*1.0/1105)   # computes the completeness valus of context features
						genre = genre + prob
						
						
						b3_genre = genre
				else:

					b3_genre = 0 			
				
				
				
				if (b4):

					sub_genre=0	

					for element in b4:
						
						element_count=0
						for movie in Movie_Details.objects.all():
							
							movie_genre11=movie.sub_genre.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							
						
						prob=1-(element_count*1.0/1105)
						sub_genre = sub_genre + prob
						
						b4_sub_genre = sub_genre
				

				else:
					b4_sub_genre = 0
				

				
				if (b5):
					director = 0
					for element in b5:
					
						element_count=0
						for movie in Movie_Details.objects.all():
							
							movie_genre11=movie.director.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							
						
						prob=1-(element_count*1.0/1105)
						director =director + prob
						
						b5_director = director
					
				
				else:
					b5_director = 0

				if (b6):	
					cast = 0
					for element in b6:
						
						element_count=0
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							movie_genre11=movie.cast.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							# for sd in movie_genre11:
						#print element,"====",element_count
						prob=1-(element_count*1.0/1105)
						cast = cast + prob
						
						b6_cast = cast
				else:
					b6_cast = 0

				if (b7):			
					based_on = 0
					for element in b7:
						
						element_count=0
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							movie_genre11=movie.based_on.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							# for sd in movie_genre11:
						#print element,"====",element_count
						prob=1-(element_count*1.0/1105)
						based_on = based_on + prob
						
						b7_based_on = based_on

				else:
					b7_based_on = 0


				if (b8):				
					about = 0
					for element in b8:
						
						element_count=0
						for movie in Movie_Details.objects.all():
							#if b3 in q.genre.split(','):
							movie_genre11=movie.about.split(',')
							if element in movie_genre11:
								element_count=element_count+1
							# for sd in movie_genre11:
						#print element,"====",element_count
						prob=1-(element_count*1.0/1105)
						about = about + prob
						
						b8_about = about

				else:		
					b8_about = 0

				if (b10):
					topics = 0
					for element in b10:
						element_count=0
						for movie in Movie_Details.objects.all():
							if movie.movie_topics_lda:
								movie_genre11=movie.movie_topics_lda.split(', ')
								if  element in movie_genre11:
									element_count=element_count+1
						prob=1-(element_count*1.0/1105)
						topics = topics + prob
						b10_movie_topics = topics	

				else:
					b10_movie_topics = 0				

				#import pdb;pdb.set_trace()	

				b12 = (b3_genre) + (b4_sub_genre) + (b5_director)  + (b6_cast) + (b7_based_on) + (b8_about)  + (b10_movie_topics)

				s_in = 1

				mindegree = min(len(genre1) + len(sub_genre1) + len(director1) + len(based_on1) + len(about1) + len(movie_topics_lda1),len(genre2) + len(sub_genre2) + len(director2)  + len(based_on2) + len(about2) + len(movie_topics_lda2) )
				
				maxdegree = max(len(genre1) + len(sub_genre1) + len(director1) + len(based_on1) + len(about1) + len(movie_topics_lda1),len(genre2) + len(sub_genre2) + len(director2) + len(based_on2) + len(about2) + len(movie_topics_lda2) )

				s_out = float(mindegree)/maxdegree

				x11 = (s_in + s_out)/2
				

				s_out_1 = (b12 * x11)/maxdegree
				x12 = (s_in + s_out_1)/2
				
				
				while(abs(x11-x12)>0.0001):

					x11 = x12
					s_in = 1
					s_out_1 = (b12 * x12)/maxdegree
					x12 = (s_in + s_out_1)/2


					final = x11
				feature_dict[k.name.encode('utf-8')] = x12
				
				
				print k.name.encode('utf-8')

				print k.id
		
		
		import operator
		
		sorted_x = sorted(feature_dict.items(), key=operator.itemgetter(1))
		
		
		for k in Movie_Details.objects.filter(id=moviename):

		

			k.movie_similarity_new = sorted_x

			k.save()

			print k.id

			print k.name