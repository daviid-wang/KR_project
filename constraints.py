from rdflib import Graph, Literal, RDF, Namespace, BNode
from pyshacl import validate

data_graph = Graph()
data_graph.parse("handbook.ttl", format="ttl")

sha_str = """
            @prefix sha: <http://www.w3.org/ns/shacl#> .
            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
            @prefix h: <http://university.org/> .



            h:unit_shape a sha:NodeShape ;
                sha:targetClass h:unit ;
                sha:sparql [
		            sha:select '''
                    PREFIX h: <http://university.org/>
                        SELECT $this ?preUnit 
                        WHERE { 
                            $this h:has_prerequisite ?preUnit . 
                            $this h:has_level ?thisLevel . 
                            ?thisLevel h:has_number ?thisNumber . 
                            ?preUnit h:has_level ?preLevel . 
                            ?preLevel h:has_number ?preNumber . 
                            FILTER (?thisNumber <= ?preNumber) .
                        } 
                    ''' ;
	        ] . 
"""


sha_graph = Graph()
sha_graph.parse(data=sha_str, format='ttl')

conforms, results_graph, results_text = validate(data_graph, shacl_graph=sha_graph)
print(results_text)