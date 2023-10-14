# from owlready2 import *
from rdflib import Graph
import sys

g = Graph()
g.parse("handbook.ttl", format="turtle")

arguments = sys.argv

if arguments[1] == "getAllMajors":
    selection = "?major"
    query = "?major a rdfs:Class ."
if arguments[1] == "getAllDescription":
    selection = "?unit ?description"
    query ="?unit handbook:has_credit ?description ."
results = g.query(
    f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX handbook: <http://university.org/#>

        SELECT {selection}
        WHERE{{
        {query}
        }}
        """)

for row in results:
    print(row)