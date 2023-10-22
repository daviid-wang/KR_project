"""
David Wang (23064035)
Hannah Doret (22846377)
"""

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

			h:major_shape a shacl:NodeShape ;
				shacl:targetClass h:major ;
				shacl:sparql [
					shacl:select '''
						PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
						PREFIX owl: <http://www.w3.org/2002/07/owl#>
						PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
						PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
						PREFIX h: <http://university.org/>

						SELECT $this ?level
						WHERE {
							$this h:has_unit ?unit .
							?unit h:has_contact_hrs ?hours .
							?unit h:has_credit ?credit .
							?unit h:has_level ?level .
							{SELECT (COUNT(?unit) AS ?zeroCount) WHERE { ?unit h:has_credit 0 . }}
						}
						GROUP BY ?level $this
						HAVING ((4 * SUM(?hours) / (COUNT(?unit) - ?zeroCount)) > 40)
					''' ;
				] .
"""

shacl_graph = Graph()
shacl_graph.parse(data=shacl_str, format='ttl')

conforms, results_graph, results_text = validate(data_graph, shacl_graph=shacl_graph)
print(results_text)