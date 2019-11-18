
 # This program extracts the properties and values from DBpedia 

def dbpedia_details(request):

	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery("""
	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>


	SELECT DISTINCT ?actor 
	WHERE {
	<http://dbpedia.org/resource/Movie_Name> <http://dbpedia.org/ontology/abstract> ?actor #Enter the movie URI instead of Movie_Name
	}

	""")
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	movie_features=[]
	movie_about=''
	movie_based_on=''
	
	
	for result in results["results"]["bindings"]: # This return the subjective property, value pair of the movie
		movie_features.append(result["actor"]["value"])

		
	# You need to provide different properties to extract different <property, value> pair.