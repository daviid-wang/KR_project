from rdflib import Graph, Literal, RDF, Namespace, BNode
from pyshacl import validate

from university import *

g = Graph()
g.parse("handbook.ttl", format="ttl")

SHACL = Namespace("http://www.w3.org/ns/shacl#")
g.bind("sh", SHACL)

shaclGraph = Graph()




# every prerequisite for a level X unit should have a level less than X
unit_shape = h.unit_shape #is this supposed to be shacl.unit_shape or h.unit_shape?????????
prereq_shape = h.unit_shape
has_level_shape = BNode()
has_prereq_shape = BNode()
shaclGraph.add((unit_shape, RDF.type, SHACL.NodeShape))
shaclGraph.add((unit_shape, SHACL.targetClass, h.unit))
shaclGraph.add((prereq_shape, RDF.type, SHACL.NodeShape))
shaclGraph.add((prereq_shape, SHACL.targetClass, h.unit))
shaclGraph.add((has_level_shape, SHACL.path, h.has_level))
shaclGraph.add((has_prereq_shape, SHACL.path, h.has_prerequisite))
shaclGraph.add((unit_shape, has_level_shape))

handbook:unit_shape a 