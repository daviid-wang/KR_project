from owlready2 import *
from rdflib import *
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















































#############################           hannah         #########################
# find all level 3 units that do not have an exam, and none of their prerequisites have an exam either
han_query = """
    SELECT ?unit WHERE 
    {
        ?unit handbook:has_level handbook:3 .
        FILTER NOT EXISTS {?unit handbook:has_assessment handbook:exam} .
        OPTIONAL {?unit handbook:has_prerequisite ?prereq} .
        FILTER NOT EXISTS {?prereq handbook:has_assessment handbook:exam} .
    }
    GROUP BY ?unit
"""

# find units that contain <search_string> in the descriptions or outcomes
# search string should probably come from user input
search_string = "amazing"
han_query2 = f"""
    SELECT ?unit WHERE
    {{
        {{
            ?unit a handbook:unit .
            ?unit handbook:has_description ?description .
            FILTER CONTAINS(?description, "{search_string}") .
        }}
        UNION
        {{
            ?unit a handbook:unit .
            ?unit handbook:has_outcome ?outcome .
            FILTER CONTAINS(?outcome, "{search_string}") .
        }}
    }}
    GROUP BY ?unit
"""

han_result = g.query(han_query2)
#for result in han_result:
#    print(result)
    