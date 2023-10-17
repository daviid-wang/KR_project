from rdflib import Graph, Literal, RDF, Namespace, BNode
from pyshacl import validate

data_graph = Graph()
data_graph.parse("handbook.ttl", format="ttl")
# sha_str = """
#             @prefix sha: <http://www.w3.org/ns/shacl#> .
#             @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
#             @prefix h: <http://university.org/> .

#             h:unit_shape a sha:NodeShape ;
#                 sha:targetClass h:unit ;

#             sha:property [
#                 sha:path h:has_level ;
#                 sha:property [
#                     sha:path h:has_number ;
#                     sha:datatype xsd:integer ;
#                 ] ;
#             ] ;
#             sha:property [
#                 sha:path h:has_prerequisite ;
#                 sha:qualifiedValueShape [
#                     sha:nodeKind sha:IRI ;
#                     sha:property [
#                         sha:path h:has_level ;
#                         sha:property [
#                             sha:path h:has_number ;
#                             sha:maxExclusive 9 ;
#                         ] ;
#                     ] ;
#                 ] ;
#                 sha:qualifiedMinCount 1 ;
#             ] .

# """


sha_str = """
            @prefix sha: <http://www.w3.org/ns/shacl#> .
            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
            @prefix h: <http://university.org/> .

            h:unit_shape a sha:NodeShape ;
                sha:targetClass h:unit ;

            sha:propertyValidator [
		        a sha:SPARQLSelectValidator ;
		        sha:select '''
			        SELECT $this ?preUnit
			        WHERE {
				    $this h:has_prerequisite ?preUnit .
                    $this h:has_level ?thisLevel .
                    ?thisLevel h:has_number ?thisNumber .
                    ?preUnit h:has_level ?preLevel .
                    ?preLevel h:has_number ?preNumber .
				    FILTER (?thisNumber > ?preNumber)
			        }
			    '''
	        ] .
"""






sha_graph = Graph()
sha_graph.parse(data=sha_str, format='ttl')

conforms, results_graph, results_text = validate(data_graph, shacl_graph=sha_graph)
print(results_text)