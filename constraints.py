from rdflib import Graph, Literal, RDF, Namespace, BNode
from pyshacl import validate

data_graph = Graph()
data_graph.parse("handbook.ttl", format="ttl")

shacl_str = """
            @prefix shacl: <http://www.w3.org/ns/shacl#> .
            @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
            @prefix h: <http://university.org/> .

            h:unit_shape a shacl:NodeShape ;
                shacl:targetClass h:unit ;
                
				# Every unit should have a board of examiners in this list
                shacl:property [
					shacl:path h:has_board_of_examiners ;
					shacl:in (
						h:01_-_Natural_and_Physical_Sciences
						h:02_-_Information_Technology
						h:03_-_Engineering_And_Related_Technologies
						h:04_-_Architecture_and_Building
						<http://university.org/05_-_Agriculture,_Environmental_and_Related_S>
						<http://university.org/05_-_Agriculture,_Environmental_and_Related_Studies>
						h:06_-_Health
						h:07_-_Education
						h:08_-_Management_and_Commerce
						h:09_-_Society_and_Culture
						h:10_-_Creative_Arts
						h:12_-_Mixed_Field_Programmes
				) ] ;

				# Every prerequisite for a level X unit should have a level less than X
                shacl:sparql [
				shacl:select '''
                    PREFIX h: <http://university.org/>
                        SELECT $this ?preUnit 
                        WHERE { 
                            $this h:has_prerequisite ?preUnit . 
                            $this h:has_level ?thisLevel . 
                            ?thisLevel h:has_number ?thisNumber . 
                            ?preUnit h:has_level ?preLevel . 
                            ?preLevel h:has_number ?preNumber . 
                            FILTER (?thisNumber <= ?preNumber) .
                        } 
                    ''' ;
                    shacl:message "The prerequisite unit's level should be less than the unit's level."
				] ;

				#No unit should be its own prerequisite
				shacl:sparql [
					shacl:select '''
						PREFIX h: <http://university.org/>
						SELECT $this 
						WHERE {
							$this h:has_prerequisite $this .
						}
					''' ;
					shacl:message "A unit cannot be its own prerequisite." ;
				] .
"""

david_query = """
	@prefix shacl: <http://www.w3.org/ns/shacl#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    @prefix h: <http://university.org/> .

    h:unit_shape a shacl:NodeShape ;
        shacl:targetClass h:unit ;
        
        #No unit should be its own prerequisite
		shacl:sparql [
			shacl:select '''
				PREFIX h: <http://university.org/>
				SELECT $this 
				WHERE {
					$this h:has_prerequisite $this .
				}
			''' ;
			shacl:message "A unit cannot be its own prerequisite." ;
		] .
"""

shacl_graph = Graph()
shacl_graph.parse(data=shacl_str, format='ttl')

conforms, results_graph, results_text = validate(data_graph, shacl_graph=shacl_graph)
print(results_text)