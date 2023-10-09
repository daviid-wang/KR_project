"""
David Wang (23064035)
Hannah Doret (22846377)
"""

from rdflib import Graph, Literal, URIRef, RDFS
from rdflib.namespace import RDF, Namespace
# from owlready2 import *
from pyshacl import validate

import json

#Open and parse json objects
with open('units.json', 'r') as units:
    units_data = json.load(units)
units.close()

with open('majors.json', 'r') as majors:
    majors_data = json.load(majors)
majors.close()

#Create Graph and Namespace
g = Graph()
h = Namespace("https://university.org/")

g.bind("handbook", h)

#Create classes
unit = h.unit
school = h.school
board_of_examiners = h.board_of_examiners
delivery_mode = h.delivery_mode
level = h.level
credit = h.credit
assessment = h.assessment
prerequisite_unit_compulsory = h.prerequisite_unit_compulsory
# prerequisite_unit_choice = h.prerequisite_unit_choice
# prerequisite_points = h.prerequisite_points
contact = h.contact

#Add Classes
g.add((unit, RDF.type, RDFS.Class))
g.add((unit, RDFS.label, Literal("Unit")))
g.add((school, RDF.type, RDFS.Class))
g.add((school, RDFS.label, Literal("School")))
g.add((board_of_examiners, RDF.type, RDFS.Class))
g.add((board_of_examiners, RDFS.label, Literal("Board of Examiners")))
g.add((delivery_mode, RDF.type, RDFS.Class))
g.add((delivery_mode, RDFS.label, Literal("Delivery Mode")))
g.add((level, RDF.type, RDFS.Class))
g.add((level, RDFS.label, Literal("Level")))
g.add((credit, RDF.type, RDFS.Class))
g.add((credit, RDFS.label, Literal("Credit")))


#Create relations
has_title = h.has_title
has_school = h.has_school
has_board_of_examiners = h.has_board_of_examiners
has_unit_delivery_mode = h.has_unit_delivery_mode
has_level = h.has_level
has_description = h.has_description
has_credit = h.has_credit

#Add relations
g.add((has_title, RDF.type, RDF.Property))
g.add((has_school, RDF.type, RDF.Property))
g.add((has_board_of_examiners, RDF.type, RDF.Property))
g.add((has_unit_delivery_mode, RDF.type, RDF.Property))
g.add((has_level, RDF.type, RDF.Property))
g.add((has_description, RDF.type, RDF.Property))
g.add((has_credit, RDF.type, RDF.Property))




#Use Json object to add to graph
i = 0

for unit_name in units_data:
    
    #Define URI
    unit_code = h[unit_name]
    unit_title = h[units_data[unit_name]["title"].replace(" ", "_")]
    unit_school = h[units_data[unit_name]["school"].replace(" ", "_")]
    unit_board_of_examiners = h[units_data[unit_name]["board_of_examiners"].replace(" ", "_")]
    unit_delivery_mode = h[units_data[unit_name]["delivery_mode"].replace(" ", "_")]
    unit_level = h[units_data[unit_name]["level"].replace(" ", "_")]
    unit_description = h[units_data[unit_name]["description"].replace(" ", "_")]
    unit_credit = h[units_data[unit_name]["credit"].replace(" ", "_")]

    # delete?
    # unit_outcomes = h[units_data[unit_name]["outcomes"].replace(" ", "_")]
    
    # unit_assessment = h[units_data[unit_name]["assessment"].replace(" ", "_")]
        
    # unit_prerequisites_text = h[units_data[unit_name]["prerequisites_text"].replace(" ", "_")]
    # unit_prerequisites_cnf = h[units_data[unit_name]["prerequisites_cnf"].replace(" ", "_")]
    # unit_advisable_prior_study = h[units_data[unit_name]["advisable_prior_study"].replace(" ", "_")]
    # unit_contact = h[units_data[unit_name]["contact"].replace(" ", "_")]
    
    
    #Name
    g.add((unit_code, RDF.type, unit))
    g.add((unit_code, RDFS.label, Literal(unit_name)))

    #Title
    g.add((unit_title, RDFS.label , Literal(units_data[unit_name]["title"])))
    
    #School
    g.add((unit_school, RDF.type, school))
    g.add((unit_school, RDFS.label, Literal(units_data[unit_name]["school"])))
    
    #Board of Examiners
    g.add((unit_board_of_examiners, RDF.type, board_of_examiners))
    g.add((unit_board_of_examiners, RDFS.label, Literal(units_data[unit_name]["board_of_examiners"])))
    
    #Delivery mode
    g.add((unit_delivery_mode, RDF.type, delivery_mode))
    g.add((unit_delivery_mode, RDFS.label, Literal(units_data[unit_name]["delivery_mode"])))
    
    #Level
    g.add((unit_level, RDF.type, level))
    g.add((unit_level, RDFS.label, Literal(units_data[unit_name]["level"])))
    
    #Description
    g.add((unit_description, RDFS.label, Literal(units_data[unit_name]["description"])))
    
    #Credit
    g.add((unit_credit, RDF.type, credit))
    g.add((unit_credit, RDFS.label, Literal(units_data[unit_name]["credit"])))
    

    for assessment_item in units_data[unit_name]["assessment"]:
        g.add((h[assessment_item.replace(" ", "_")], RDF.type, assessment))
        g.add((h[assessment_item.replace(" ", "_")], RDFS.label, Literal(assessment_item)))
    
    #Add relations to graph
    g.add((unit_code, has_title, unit_title))
    g.add((unit_code, has_school, unit_school))
    g.add((unit_code, has_board_of_examiners, unit_board_of_examiners))
    g.add((unit_code, has_unit_delivery_mode, unit_delivery_mode))
    g.add((unit_code, has_level, unit_level))
    g.add((unit_code, has_description, unit_description))
    g.add((unit_code, has_credit, unit_credit))
    
    # i += 1
    # if i == 5:
    #     break

results = g.query("""
    PREFIX handbook: <https://university.org/>
    
    SELECT ?unit ?description 
    WHERE {
        ?unit handbook:has_description ?description .
    }
""")

# for result in results:
#     print(result)

# print graph
print(g.serialize(destination = "handbook.ttl", format='ttl', indent=4))