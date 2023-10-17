# from owlready2 import *
from rdflib import Graph
import sys

g = Graph()
g.parse("handbook.ttl", format="turtle")

arguments = sys.argv

selection = ""
additional = ""

if arguments[1] == "getAllClasses":
    selection = "?major"
    query = """
        ?major a rdfs:Class .
    """

if arguments[1] == "getDescription":
    selection = "?description"
    query =f"""
        handbook:{arguments[2]} handbook:has_description ?description .
    """

if arguments[1] == "getUnitsWithOutcomes":
    selection = "?unit"
    query = """
        ?unit a handbook:unit . 
        ?unit handbook:has_outcome ?outcomes .
    """
    additional = f"""
        GROUP BY ?unit 
        HAVING (COUNT(?outcomes) > {arguments[2]})
    """

if arguments[1] == "noExamUnit":
    selection = "?unit"
    query = """
        ?unit handbook:has_level handbook:3 .
        FILTER NOT EXISTS {?unit handbook:has_assessment handbook:exam} .
        OPTIONAL {?unit handbook:has_prerequisite ?prereq} .
        FILTER NOT EXISTS {?prereq handbook:has_assessment handbook:exam} .
    """
    additional = """
        GROUP BY ?unit
    """

if arguments[1] == "getUnitsWithMajors":
    selection = "?unit"
    query = """
        ?unit a handbook:unit . 
        ?unit handbook:has_major ?major .
    """
    additional = f"""
        GROUP BY ?unit 
        HAVING (COUNT(?major) > 3)
    """

# find units that contain <search_string> in the descriptions or outcomes
# search string should probably come from user input
if arguments[1] == "search":
    selection = "?unit"
    query = f"""
        {{
            ?unit a handbook:unit .
            ?unit handbook:has_description ?description .
            FILTER CONTAINS(?description, "{arguments[2]}") .
        }}
        UNION
        {{
            ?unit a handbook:unit .
            ?unit handbook:has_outcome ?outcome .
            FILTER CONTAINS(?outcome, "{arguments[2]}") .
        }}
    """

# Throw Error if exception
if selection == "":
    raise Exception("Incorrect argument")

results = g.query(
    f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX handbook: <http://university.org/>

        SELECT {selection}
        WHERE{{
        {query}
        }}
        {additional}
        """)


for row in results:
    print(row[0])
