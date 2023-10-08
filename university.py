"""
David Wang 23064035
Hannah Doret 22846377
"""

from rdflib import Graph, Literal, RDF, URIRef, RDFS
from rdflib.namespace import *
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


#Create relations
has_school = h.has_school

#Add relations
g.add((has_school, RDF.type, RDF.Property))




#Use Json object to add to graph
i = 0

for unit_name in units_data:
    
    unit_code = h[unit_name]
    print(unit_code)
    unit_school = h[units_data[unit_name]["school"].replace(" ", "_")]
    print(unit_school)
    # CITS3200 = h[CITS3200]
    g.add((unit_code, RDF.type, unit))
    g.add((unit_code, RDFS.label, Literal(unit_name)))
    g.add((unit_school, RDF.type, school))
    g.add((unit_school, RDFS.label, Literal(units_data[unit_name]["school"])))
    
    g.add((unit_code, has_school, unit_school))
    i += 1
    if i == 5:
        break





#print graph
print(g.serialize(format='ttl', indent=4))