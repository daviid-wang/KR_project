from rdflib import Graph, Literal, RDF, Namespace, BNode
from pyshacl import validate

data_graph = Graph()
data_graph.parse("handbook.ttl", format="ttl")
sha_str = """
            @prefix sha: <http://www.w3.org/ns/shacl#> .
            @prefix h: <http://university.org#> .

            h:unit_shape a sha:NodeShape ;
                sha:targetClass h:unit ;

            sha:property [
                sha:path h:has_level ;
                sha:property [
                    sha:path h:has_number ;
                    sha:minCount 1 ;
                ] ;
            ] ;
            sha:property [
                sha:path h:has_prerequisite ;
                sha:qualifiedValueShape [
                    sha:property [
                        sha:path h:has_level ;
                        sha:property [
                            sha:path h:has_number ;
                            sha:maxExclusive ???? ;
                        ] ;
                    ] ;
                ] ;
            ] .

"""
sha_graph = Graph()
sha_graph.parse(data=sha_str, format='ttl')

conforms, results_graph, results_text = validate(data_graph, shacl_graph=sha_graph)
print(results_text)