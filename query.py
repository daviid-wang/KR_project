from owlready2 import *
import sys

g = Graph()
g.parse("handbook.ttl", format="turtle")

arguments = sys.argv

if arguments[1] == "getAllMajors":
    selection = "?major"
    query = "?major a handbook:major ."

results = default_world.sparql(
    f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX pokemon: <http://test.org/pokemon#>

        SELECT {selection}
        WHERE{{
        {query}
        }}
        """)

for result in results:
    print(result)