# from owlready2 import *
from rdflib import Graph
import sys

g = Graph()
g.parse("handbook.ttl", format="turtle")

arguments = sys.argv

if arguments[1] == "getAllClasses":
    selection = "?major"
    query = "?major a rdfs:Class ."
    additional = ""
if arguments[1] == "getDescription":
    selection = "?description"
    query =f"handbook:{arguments[2]} handbook:has_description ?description ."
    additional = ""
if arguments[1] == "getUnitsWithOutcomes":
    selection = "?unit"
    query = "?unit a handbook:unit . ?unit handbook:has_outcome ?outcomes ."
    additional = f"GROUP BY ?unit HAVING (COUNT(?outcomes) > {arguments[2]})"


results = g.query(
    f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX handbook: <https://university.org/>

        SELECT {selection}
        WHERE{{
        {query}
        }}
        {additional}
        """)




for row in results:
    print(row)
    
    
# test_query = """
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#         PREFIX owl: <http://www.w3.org/2002/07/owl#>
#         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#         PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
#         PREFIX handbook: <https://university.org/>

#         SELECT ?unit WHERE {
#             ?unit a handbook:unit .
#             ?unit handbook:has_outcome ?outcomes .
#         }
#         GROUP BY ?unit
#         HAVING (COUNT(?outcomes) > 6)
#         """
# test_results = g.query(test_query)
# for result in test_results:
#     print(result[0])