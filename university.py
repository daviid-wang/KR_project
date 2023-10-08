from rdflib import *
from rdflib.namespace import *
from rdflib.serializer import Serializer
from owlready2 import *
from pyshacl import validate

import json

handbook = Graph().parse(data='./units.json', format='n3')

print(handbook.serialize(format='json-ld', indent=4))