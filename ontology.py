from owlready2 import *

onto = get_ontology("http://university.org")

with onto:
    class Unit(Thing): pass
    
    
    
    
    
    
    
    
    
    
    
    
    onto.save(file = "handbook.owl", format = "rdfxml")