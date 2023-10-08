"""
David Wang 23064035
Hannah Doret 22846377
"""

from rdflib import *
from rdflib.namespace import *
from rdflib.serializer import Serializer
from owlready2 import *
from pyshacl import validate

import json

with open('units.json', 'r') as units:
    units_data = json.load(units)
    # print(units_data)

print(units_data['AGRI5403']["code"])

handbook = Graph()
# .parse(filename= './units.json', format='n3')

# print(handbook.serialize(format='json-ld', indent=4))