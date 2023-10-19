Validation Report
Conforms: False
Results (672):
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:major_shape
	Focus Node: handbook:MJD-MSTGM
	Value Node: handbook:MJD-MSTGM
	Source Constraint: [ shacl:select Literal("
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
					") ]
Constraint Violation in InConstraintComponent (http://www.w3.org/ns/shacl#InConstraintComponent):
	Severity: shacl:Violation
	Source Shape: [ shacl:in ( h:01_-_Natural_and_Physical_Sciences h:02_-_Information_Technology h:03_-_Engineering_And_Related_Technologies h:04_-_Architecture_and_Building <http://university.org/05_-_Agriculture,_Environmental_and_Related_S> <http://university.org/05_-_Agriculture,_Environmental_and_Related_Studies> h:06_-_Health h:07_-_Education h:08_-_Management_and_Commerce h:09_-_Society_and_Culture h:10_-_Creative_Arts h:12_-_Mixed_Field_Programmes ) ; shacl:path h:has_board_of_examiners ]
	Focus Node: handbook:SCIE1500
	Value Node: handbook:05
	Result Path: h:has_board_of_examiners
	Message: Value handbook:05 not in list ['<http://university.org/05_-_Agriculture,_Environmental_and_Related_S>', 'h:03_-_Engineering_And_Related_Technologies', 'h:07_-_Education', 'h:10_-_Creative_Arts', 'h:09_-_Society_and_Culture', '<http://university.org/05_-_Agriculture,_Environmental_and_Related_Studies>', 'h:12_-_Mixed_Field_Programmes', 'h:06_-_Health', 'h:08_-_Management_and_Commerce', 'h:02_-_Information_Technology', 'h:01_-_Natural_and_Physical_Sciences', 'h:04_-_Architecture_and_Building']
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5902
	Value Node: handbook:RMED5902
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5337
	Value Node: handbook:PODI5337
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5415
	Value Node: handbook:IMED5415
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM4106
	Value Node: handbook:OPTM4106
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED2004
	Value Node: handbook:IMED2004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4226
	Value Node: handbook:PODI4226
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS5017
	Value Node: handbook:CITS5017
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6904
	Value Node: handbook:DENT6904
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:HRMT5518
	Value Node: handbook:HRMT5518
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BMED4006
	Value Node: handbook:BMED4006
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHCY5615
	Value Node: handbook:PHCY5615
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PAED5702
	Value Node: handbook:PAED5702
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHPR3407
	Value Node: handbook:CHPR3407
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BMED4005
	Value Node: handbook:BMED4005
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5335
	Value Node: handbook:PODI5335
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEM2103
	Value Node: handbook:CHEM2103
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:KORE1406
	Value Node: handbook:KORE1406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6910
	Value Node: handbook:DENT6910
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5520
	Value Node: handbook:FINA5520
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS1021
	Value Node: handbook:PHYS1021
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5527
	Value Node: handbook:FINA5527
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SURG5855
	Value Node: handbook:SURG5855
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5533
	Value Node: handbook:EDUC5533
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED1004
	Value Node: handbook:IMED1004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS5013
	Value Node: handbook:CITS5013
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC4422
	Value Node: handbook:PSYC4422
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6846
	Value Node: handbook:DENT6846
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5836
	Value Node: handbook:IMED5836
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEOS4017
	Value Node: handbook:GEOS4017
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SMED5322
	Value Node: handbook:SMED5322
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:KORE2404
	Value Node: handbook:KORE2404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5586
	Value Node: handbook:PSYC5586
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5255
	Value Node: handbook:LAWS5255
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GENG5522
	Value Node: handbook:GENG5522
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ANHB5457
	Value Node: handbook:ANHB5457
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6909
	Value Node: handbook:DENT6909
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN1402
	Value Node: handbook:GRMN1402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5633
	Value Node: handbook:ACCT5633
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PUBH5802
	Value Node: handbook:PUBH5802
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5810
	Value Node: handbook:IMED5810
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6822
	Value Node: handbook:DENT6822
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ECON5504
	Value Node: handbook:ECON5504
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6864
	Value Node: handbook:DENT6864
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5194
	Value Node: handbook:PATH5194
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARTF3050
	Value Node: handbook:ARTF3050
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6874
	Value Node: handbook:DENT6874
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5475
	Value Node: handbook:EDUC5475
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6902
	Value Node: handbook:DENT6902
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC2525
	Value Node: handbook:MUSC2525
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN2405
	Value Node: handbook:FREN2405
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BLDG5800
	Value Node: handbook:BLDG5800
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5307
	Value Node: handbook:PODI5307
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARCY2005
	Value Node: handbook:ARCY2005
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS3044
	Value Node: handbook:PHYS3044
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5321
	Value Node: handbook:RMED5321
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6805
	Value Node: handbook:DENT6805
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS4113
	Value Node: handbook:LAWS4113
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6903
	Value Node: handbook:DENT6903
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:AHEA3300
	Value Node: handbook:AHEA3300
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5740
	Value Node: handbook:EDUC5740
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEOS5511
	Value Node: handbook:GEOS5511
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SCIE1104
	Value Node: handbook:SCIE1104
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6806
	Value Node: handbook:DENT6806
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5615
	Value Node: handbook:MGMT5615
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN1406
	Value Node: handbook:CHIN1406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED3020
	Value Node: handbook:IMED3020
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BLDG5801
	Value Node: handbook:BLDG5801
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ANHB5434
	Value Node: handbook:ANHB5434
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ECON5006
	Value Node: handbook:ECON5006
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:URBD5801
	Value Node: handbook:URBD5801
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5323
	Value Node: handbook:RMED5323
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5730
	Value Node: handbook:EDUC5730
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS1200
	Value Node: handbook:PHYS1200
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYL5513
	Value Node: handbook:PHYL5513
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5502
	Value Node: handbook:MGMT5502
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5404
	Value Node: handbook:DENT5404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SRUR5322
	Value Node: handbook:SRUR5322
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EMED5504
	Value Node: handbook:EMED5504
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5674
	Value Node: handbook:PSYC5674
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5116
	Value Node: handbook:PATH5116
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:URBD5806
	Value Node: handbook:URBD5806
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM5103
	Value Node: handbook:OPTM5103
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5181
	Value Node: handbook:PATH5181
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ANHB3322
	Value Node: handbook:ANHB3322
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ANHB2213
	Value Node: handbook:ANHB2213
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5531
	Value Node: handbook:FINA5531
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5697
	Value Node: handbook:LAWS5697
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC2542
	Value Node: handbook:MUSC2542
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6809
	Value Node: handbook:DENT6809
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6839
	Value Node: handbook:DENT6839
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATH1014
	Value Node: handbook:MATH1014
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5531
	Value Node: handbook:PSYC5531
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN1404
	Value Node: handbook:FREN1404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARCT5302
	Value Node: handbook:ARCT5302
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5414
	Value Node: handbook:IMED5414
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5514
	Value Node: handbook:PODI5514
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHCY5602
	Value Node: handbook:PHCY5602
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OCEN5004
	Value Node: handbook:OCEN5004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INDO2406
	Value Node: handbook:INDO2406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SRUR5411
	Value Node: handbook:SRUR5411
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4203
	Value Node: handbook:PODI4203
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC3572
	Value Node: handbook:MUSC3572
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5901
	Value Node: handbook:RMED5901
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHCY5632
	Value Node: handbook:PHCY5632
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED2003
	Value Node: handbook:IMED2003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYL3004
	Value Node: handbook:PHYL3004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6810
	Value Node: handbook:DENT6810
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARCT5201
	Value Node: handbook:ARCT5201
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS5036
	Value Node: handbook:PHYS5036
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARCT5102
	Value Node: handbook:ARCT5102
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SRUR5341
	Value Node: handbook:SRUR5341
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS5016
	Value Node: handbook:PHYS5016
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ECON5003
	Value Node: handbook:ECON5003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED4202
	Value Node: handbook:GMED4202
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4225
	Value Node: handbook:PODI4225
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ECON5506
	Value Node: handbook:ECON5506
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PAED5503
	Value Node: handbook:PAED5503
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5904
	Value Node: handbook:PSYC5904
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN1402
	Value Node: handbook:JAPN1402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC4712
	Value Node: handbook:MUSC4712
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5618
	Value Node: handbook:EDUC5618
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SCIE5520
	Value Node: handbook:SCIE5520
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6906
	Value Node: handbook:DENT6906
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5613
	Value Node: handbook:PSYC5613
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP3002
	Value Node: handbook:SWSP3002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5802
	Value Node: handbook:IMED5802
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BMEG5552
	Value Node: handbook:BMEG5552
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEND3904
	Value Node: handbook:GEND3904
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:HRMT5501
	Value Node: handbook:HRMT5501
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:KORE2406
	Value Node: handbook:KORE2406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC3542
	Value Node: handbook:MUSC3542
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5872
	Value Node: handbook:LAWS5872
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5476
	Value Node: handbook:EDUC5476
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CLAN2103
	Value Node: handbook:CLAN2103
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5620
	Value Node: handbook:EDUC5620
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEOP4013
	Value Node: handbook:GEOP4013
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC3592
	Value Node: handbook:MUSC3592
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6878
	Value Node: handbook:DENT6878
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6803
	Value Node: handbook:DENT6803
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5132
	Value Node: handbook:PATH5132
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT6793
	Value Node: handbook:MGMT6793
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP5620
	Value Node: handbook:SWSP5620
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL3407
	Value Node: handbook:ITAL3407
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5702
	Value Node: handbook:ACCT5702
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6884
	Value Node: handbook:DENT6884
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEOS5013
	Value Node: handbook:GEOS5013
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6829
	Value Node: handbook:DENT6829
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6842
	Value Node: handbook:DENT6842
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEM3103
	Value Node: handbook:CHEM3103
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC2592
	Value Node: handbook:MUSC2592
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM5202
	Value Node: handbook:OPTM5202
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARCT5202
	Value Node: handbook:ARCT5202
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ANHB5454
	Value Node: handbook:ANHB5454
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN3406
	Value Node: handbook:FREN3406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN3406
	Value Node: handbook:JAPN3406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN3408
	Value Node: handbook:GRMN3408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OCEN5412
	Value Node: handbook:OCEN5412
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT3006
	Value Node: handbook:DENT3006
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC1322
	Value Node: handbook:MUSC1322
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5584
	Value Node: handbook:PSYC5584
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4221
	Value Node: handbook:DENT4221
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4234
	Value Node: handbook:DENT4234
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PAED5706
	Value Node: handbook:PAED5706
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP9905
	Value Node: handbook:SWSP9905
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5555
	Value Node: handbook:FINA5555
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC4104
	Value Node: handbook:MUSC4104
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5193
	Value Node: handbook:PATH5193
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5172
	Value Node: handbook:PATH5172
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PUBH5758
	Value Node: handbook:PUBH5758
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM4105
	Value Node: handbook:OPTM4105
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5703
	Value Node: handbook:ACCT5703
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN2405
	Value Node: handbook:JAPN2405
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5603
	Value Node: handbook:FINA5603
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4000
	Value Node: handbook:PODI4000
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5523
	Value Node: handbook:MGMT5523
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL3406
	Value Node: handbook:ITAL3406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5115
	Value Node: handbook:LAWS5115
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS3046
	Value Node: handbook:PHYS3046
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARCT5507
	Value Node: handbook:ARCT5507
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BIOC4001
	Value Node: handbook:BIOC4001
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INDO2408
	Value Node: handbook:INDO2408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC3582
	Value Node: handbook:MUSC3582
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4211
	Value Node: handbook:DENT4211
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6879
	Value Node: handbook:DENT6879
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INDO2404
	Value Node: handbook:INDO2404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN2408
	Value Node: handbook:GRMN2408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN2409
	Value Node: handbook:GRMN2409
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEM3002
	Value Node: handbook:CHEM3002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6856
	Value Node: handbook:DENT6856
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL2406
	Value Node: handbook:ITAL2406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MKTG5604
	Value Node: handbook:MKTG5604
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FNSC5650
	Value Node: handbook:FNSC5650
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ANHB3315
	Value Node: handbook:ANHB3315
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5635
	Value Node: handbook:FINA5635
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5517
	Value Node: handbook:PSYC5517
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS4011
	Value Node: handbook:CITS4011
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5618
	Value Node: handbook:MGMT5618
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5521
	Value Node: handbook:FINA5521
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6804
	Value Node: handbook:DENT6804
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4205
	Value Node: handbook:PODI4205
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5536
	Value Node: handbook:PSYC5536
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CIVL2008
	Value Node: handbook:CIVL2008
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5721
	Value Node: handbook:EDUC5721
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5412
	Value Node: handbook:RMED5412
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6912
	Value Node: handbook:DENT6912
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6815
	Value Node: handbook:DENT6815
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5516
	Value Node: handbook:EDUC5516
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OCEN5005
	Value Node: handbook:OCEN5005
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5524
	Value Node: handbook:FINA5524
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6816
	Value Node: handbook:DENT6816
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS3011
	Value Node: handbook:PHYS3011
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:STAT1520
	Value Node: handbook:STAT1520
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BMED3003
	Value Node: handbook:BMED3003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS3012
	Value Node: handbook:PHYS3012
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5118
	Value Node: handbook:PATH5118
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS1402
	Value Node: handbook:CITS1402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5305
	Value Node: handbook:PODI5305
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN2004
	Value Node: handbook:CHIN2004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC3586
	Value Node: handbook:MUSC3586
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC1442
	Value Node: handbook:MUSC1442
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED5402
	Value Node: handbook:GMED5402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEND3901
	Value Node: handbook:GEND3901
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CLAN3204
	Value Node: handbook:CLAN3204
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5545
	Value Node: handbook:PSYC5545
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6812
	Value Node: handbook:DENT6812
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT6795
	Value Node: handbook:MGMT6795
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARTF4005
	Value Node: handbook:ARTF4005
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN1402
	Value Node: handbook:FREN1402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INDO3408
	Value Node: handbook:INDO3408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GENG1000
	Value Node: handbook:GENG1000
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5637
	Value Node: handbook:ACCT5637
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:KORE1404
	Value Node: handbook:KORE1404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5647
	Value Node: handbook:MGMT5647
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS4107
	Value Node: handbook:LAWS4107
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:STAT1401
	Value Node: handbook:STAT1401
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS5012
	Value Node: handbook:CITS5012
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEND2902
	Value Node: handbook:GEND2902
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5405
	Value Node: handbook:DENT5405
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SURG5854
	Value Node: handbook:SURG5854
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEX1002
	Value Node: handbook:CHEX1002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN1003
	Value Node: handbook:CHIN1003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:HUMA4141
	Value Node: handbook:HUMA4141
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATH1012
	Value Node: handbook:MATH1012
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHCY5614
	Value Node: handbook:PHCY5614
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SRUR5342
	Value Node: handbook:SRUR5342
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MECH5551
	Value Node: handbook:MECH5551
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS4002
	Value Node: handbook:CITS4002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EMPL5501
	Value Node: handbook:EMPL5501
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEND4141
	Value Node: handbook:GEND4141
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5537
	Value Node: handbook:PSYC5537
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5313
	Value Node: handbook:DENT5313
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INDO1402
	Value Node: handbook:INDO1402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SCIE1500
	Value Node: handbook:SCIE1500
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5176
	Value Node: handbook:LAWS5176
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BIOC1001
	Value Node: handbook:BIOC1001
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC2208
	Value Node: handbook:PSYC2208
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4201
	Value Node: handbook:PODI4201
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5338
	Value Node: handbook:PODI5338
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5596
	Value Node: handbook:LAWS5596
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC2982
	Value Node: handbook:MUSC2982
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ENSC1004
	Value Node: handbook:ENSC1004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS4202
	Value Node: handbook:LAWS4202
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS1401
	Value Node: handbook:CITS1401
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MECH4552
	Value Node: handbook:MECH4552
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5664
	Value Node: handbook:PSYC5664
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5663
	Value Node: handbook:PSYC5663
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED3112
	Value Node: handbook:IMED3112
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:WILG5003
	Value Node: handbook:WILG5003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP3007
	Value Node: handbook:SWSP3007
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6892
	Value Node: handbook:DENT6892
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5527
	Value Node: handbook:PSYC5527
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC1592
	Value Node: handbook:MUSC1592
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SRUR5321
	Value Node: handbook:SRUR5321
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL3410
	Value Node: handbook:ITAL3410
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5342
	Value Node: handbook:DENT5342
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PUBH5714
	Value Node: handbook:PUBH5714
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEM1002
	Value Node: handbook:CHEM1002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:STAT1400
	Value Node: handbook:STAT1400
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP5429
	Value Node: handbook:SWSP5429
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GENG2004
	Value Node: handbook:GENG2004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5114
	Value Node: handbook:PATH5114
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5529
	Value Node: handbook:FINA5529
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5639
	Value Node: handbook:DENT5639
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATH1721
	Value Node: handbook:MATH1721
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5508
	Value Node: handbook:EDUC5508
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SRUR5412
	Value Node: handbook:SRUR5412
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED5401
	Value Node: handbook:GMED5401
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL3408
	Value Node: handbook:ITAL3408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5632
	Value Node: handbook:FINA5632
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEOS5017
	Value Node: handbook:GEOS5017
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GENG5512
	Value Node: handbook:GENG5512
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARTF4003
	Value Node: handbook:ARTF4003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5472
	Value Node: handbook:EDUC5472
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5814
	Value Node: handbook:IMED5814
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS1001
	Value Node: handbook:PHYS1001
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL2404
	Value Node: handbook:ITAL2404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BUSN5007
	Value Node: handbook:BUSN5007
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED3004
	Value Node: handbook:IMED3004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN2814
	Value Node: handbook:GRMN2814
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5536
	Value Node: handbook:EDUC5536
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5525
	Value Node: handbook:PSYC5525
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SCIE4402
	Value Node: handbook:SCIE4402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5526
	Value Node: handbook:FINA5526
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GENE4001
	Value Node: handbook:GENE4001
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5162
	Value Node: handbook:PATH5162
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5011
	Value Node: handbook:EDUC5011
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN2812
	Value Node: handbook:FREN2812
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6905
	Value Node: handbook:DENT6905
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5341
	Value Node: handbook:DENT5341
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6811
	Value Node: handbook:DENT6811
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP5309
	Value Node: handbook:SWSP5309
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5631
	Value Node: handbook:FINA5631
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN2410
	Value Node: handbook:GRMN2410
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARLA4002
	Value Node: handbook:ARLA4002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SMED5342
	Value Node: handbook:SMED5342
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4231
	Value Node: handbook:DENT4231
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6890
	Value Node: handbook:DENT6890
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED3003
	Value Node: handbook:IMED3003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SCIE1106
	Value Node: handbook:SCIE1106
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED5403
	Value Node: handbook:GMED5403
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5443
	Value Node: handbook:DENT5443
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6880
	Value Node: handbook:DENT6880
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GENG2012
	Value Node: handbook:GENG2012
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5510
	Value Node: handbook:FINA5510
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5805
	Value Node: handbook:IMED5805
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6875
	Value Node: handbook:DENT6875
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BIOL2204
	Value Node: handbook:BIOL2204
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN2404
	Value Node: handbook:JAPN2404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SOCS4141
	Value Node: handbook:SOCS4141
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC3584
	Value Node: handbook:MUSC3584
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PLNG4401
	Value Node: handbook:PLNG4401
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5534
	Value Node: handbook:PSYC5534
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5888
	Value Node: handbook:FINA5888
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6858
	Value Node: handbook:DENT6858
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC2277
	Value Node: handbook:MUSC2277
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5401
	Value Node: handbook:DENT5401
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5678
	Value Node: handbook:PSYC5678
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5831
	Value Node: handbook:IMED5831
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4212
	Value Node: handbook:PODI4212
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5408
	Value Node: handbook:DENT5408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN3406
	Value Node: handbook:CHIN3406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN2408
	Value Node: handbook:JAPN2408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5903
	Value Node: handbook:PSYC5903
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEX1001
	Value Node: handbook:CHEX1001
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS1030
	Value Node: handbook:PHYS1030
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6886
	Value Node: handbook:DENT6886
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5413
	Value Node: handbook:RMED5413
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ENVT5566
	Value Node: handbook:ENVT5566
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PAED5505
	Value Node: handbook:PAED5505
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:STAT4063
	Value Node: handbook:STAT4063
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP4007
	Value Node: handbook:SWSP4007
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5152
	Value Node: handbook:PATH5152
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6824
	Value Node: handbook:DENT6824
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INDO3406
	Value Node: handbook:INDO3406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5812
	Value Node: handbook:IMED5812
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5548
	Value Node: handbook:PSYC5548
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC9986
	Value Node: handbook:EDUC9986
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GENG4412
	Value Node: handbook:GENG4412
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5701
	Value Node: handbook:ACCT5701
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6848
	Value Node: handbook:DENT6848
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5158
	Value Node: handbook:LAWS5158
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS3001
	Value Node: handbook:PHYS3001
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5505
	Value Node: handbook:MGMT5505
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5312
	Value Node: handbook:IMED5312
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:HERI5110
	Value Node: handbook:HERI5110
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5336
	Value Node: handbook:PODI5336
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN3410
	Value Node: handbook:CHIN3410
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5162
	Value Node: handbook:LAWS5162
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6887
	Value Node: handbook:DENT6887
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYL5514
	Value Node: handbook:PHYL5514
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5168
	Value Node: handbook:LAWS5168
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN2406
	Value Node: handbook:JAPN2406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5142
	Value Node: handbook:PATH5142
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5500
	Value Node: handbook:EDUC5500
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MEDC5804
	Value Node: handbook:MEDC5804
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN2404
	Value Node: handbook:FREN2404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHCY5630
	Value Node: handbook:PHCY5630
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SMED5341
	Value Node: handbook:SMED5341
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5521
	Value Node: handbook:ACCT5521
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN2404
	Value Node: handbook:CHIN2404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MECH2004
	Value Node: handbook:MECH2004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SPAN2404
	Value Node: handbook:SPAN2404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC2442
	Value Node: handbook:MUSC2442
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5135
	Value Node: handbook:LAWS5135
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED4222
	Value Node: handbook:IMED4222
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN2407
	Value Node: handbook:GRMN2407
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH2222
	Value Node: handbook:PATH2222
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5415
	Value Node: handbook:DENT5415
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6872
	Value Node: handbook:DENT6872
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS1100
	Value Node: handbook:PHYS1100
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SCIE5005
	Value Node: handbook:SCIE5005
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5641
	Value Node: handbook:DENT5641
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ENVE4552
	Value Node: handbook:ENVE4552
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN3406
	Value Node: handbook:GRMN3406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5720
	Value Node: handbook:EDUC5720
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MECH5552
	Value Node: handbook:MECH5552
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:AGRI5403
	Value Node: handbook:AGRI5403
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN1406
	Value Node: handbook:GRMN1406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4211
	Value Node: handbook:PODI4211
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYX0030
	Value Node: handbook:PHYX0030
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5192
	Value Node: handbook:PATH5192
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP5634
	Value Node: handbook:SWSP5634
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5513
	Value Node: handbook:PODI5513
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS5015
	Value Node: handbook:CITS5015
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5535
	Value Node: handbook:EDUC5535
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5470
	Value Node: handbook:EDUC5470
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OCEN5512
	Value Node: handbook:OCEN5512
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS2402
	Value Node: handbook:CITS2402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5445
	Value Node: handbook:DENT5445
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PAED5707
	Value Node: handbook:PAED5707
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PAED5506
	Value Node: handbook:PAED5506
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5541
	Value Node: handbook:EDUC5541
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5108
	Value Node: handbook:LAWS5108
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM5201
	Value Node: handbook:OPTM5201
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ANHB5453
	Value Node: handbook:ANHB5453
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL3409
	Value Node: handbook:ITAL3409
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5538
	Value Node: handbook:PSYC5538
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SPAN1402
	Value Node: handbook:SPAN1402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6823
	Value Node: handbook:DENT6823
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4207
	Value Node: handbook:PODI4207
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN1406
	Value Node: handbook:JAPN1406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5413
	Value Node: handbook:IMED5413
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5421
	Value Node: handbook:IMED5421
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS5436
	Value Node: handbook:PHYS5436
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PAED5708
	Value Node: handbook:PAED5708
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATX0721
	Value Node: handbook:MATX0721
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHAR2220
	Value Node: handbook:PHAR2220
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LACH5504
	Value Node: handbook:LACH5504
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6845
	Value Node: handbook:DENT6845
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5528
	Value Node: handbook:MGMT5528
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5521
	Value Node: handbook:EDUC5521
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5835
	Value Node: handbook:IMED5835
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ANHB5433
	Value Node: handbook:ANHB5433
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN2408
	Value Node: handbook:FREN2408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6847
	Value Node: handbook:DENT6847
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED5220
	Value Node: handbook:GMED5220
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5511
	Value Node: handbook:MGMT5511
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED5602
	Value Node: handbook:GMED5602
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEOS5504
	Value Node: handbook:GEOS5504
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ECON5540
	Value Node: handbook:ECON5540
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS4022
	Value Node: handbook:PHYS4022
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6889
	Value Node: handbook:DENT6889
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4233
	Value Node: handbook:DENT4233
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5403
	Value Node: handbook:DENT5403
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5805
	Value Node: handbook:RMED5805
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PPHE4141
	Value Node: handbook:PPHE4141
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5448
	Value Node: handbook:DENT5448
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM5104
	Value Node: handbook:OPTM5104
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5512
	Value Node: handbook:PODI5512
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHCY5616
	Value Node: handbook:PHCY5616
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP5621
	Value Node: handbook:SWSP5621
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FNSC5626
	Value Node: handbook:FNSC5626
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5513
	Value Node: handbook:MGMT5513
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6828
	Value Node: handbook:DENT6828
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5534
	Value Node: handbook:EDUC5534
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN3408
	Value Node: handbook:JAPN3408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5679
	Value Node: handbook:PSYC5679
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4227
	Value Node: handbook:PODI4227
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6908
	Value Node: handbook:DENT6908
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHPR1005
	Value Node: handbook:CHPR1005
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN2406
	Value Node: handbook:FREN2406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:KORE1402
	Value Node: handbook:KORE1402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6859
	Value Node: handbook:DENT6859
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEM3104
	Value Node: handbook:CHEM3104
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4208
	Value Node: handbook:PODI4208
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PUBH2203
	Value Node: handbook:PUBH2203
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP5603
	Value Node: handbook:SWSP5603
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ENVE5552
	Value Node: handbook:ENVE5552
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5515
	Value Node: handbook:EDUC5515
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ELEC5552
	Value Node: handbook:ELEC5552
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4206
	Value Node: handbook:PODI4206
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5414
	Value Node: handbook:DENT5414
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4235
	Value Node: handbook:DENT4235
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED1003
	Value Node: handbook:IMED1003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5706
	Value Node: handbook:ACCT5706
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN1403
	Value Node: handbook:CHIN1403
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5705
	Value Node: handbook:ACCT5705
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:HRMT2237
	Value Node: handbook:HRMT2237
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6840
	Value Node: handbook:DENT6840
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GEOS4013
	Value Node: handbook:GEOS4013
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MECH4551
	Value Node: handbook:MECH4551
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5806
	Value Node: handbook:RMED5806
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5608
	Value Node: handbook:MGMT5608
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5307
	Value Node: handbook:DENT5307
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHCY5612
	Value Node: handbook:PHCY5612
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS3003
	Value Node: handbook:PHYS3003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP5409
	Value Node: handbook:SWSP5409
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATH1011
	Value Node: handbook:MATH1011
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED5702
	Value Node: handbook:GMED5702
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4216
	Value Node: handbook:DENT4216
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5526
	Value Node: handbook:PSYC5526
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5533
	Value Node: handbook:PSYC5533
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5531
	Value Node: handbook:ACCT5531
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS3100
	Value Node: handbook:PHYS3100
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6894
	Value Node: handbook:DENT6894
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATX1722
	Value Node: handbook:MATX1722
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATX1721
	Value Node: handbook:MATX1721
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ECON5005
	Value Node: handbook:ECON5005
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL1402
	Value Node: handbook:ITAL1402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP9906
	Value Node: handbook:SWSP9906
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6835
	Value Node: handbook:DENT6835
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5523
	Value Node: handbook:FINA5523
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN2408
	Value Node: handbook:CHIN2408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4219
	Value Node: handbook:DENT4219
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN1403
	Value Node: handbook:JAPN1403
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SCIE4002
	Value Node: handbook:SCIE4002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6818
	Value Node: handbook:DENT6818
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5305
	Value Node: handbook:DENT5305
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED4444
	Value Node: handbook:IMED4444
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS5563
	Value Node: handbook:PHYS5563
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5010
	Value Node: handbook:EDUC5010
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5523
	Value Node: handbook:PSYC5523
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ENSC3018
	Value Node: handbook:ENSC3018
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS5026
	Value Node: handbook:PHYS5026
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5411
	Value Node: handbook:IMED5411
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6834
	Value Node: handbook:DENT6834
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL1406
	Value Node: handbook:ITAL1406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SMED5412
	Value Node: handbook:SMED5412
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:POLS5682
	Value Node: handbook:POLS5682
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN2404
	Value Node: handbook:GRMN2404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA3333
	Value Node: handbook:FINA3333
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN1404
	Value Node: handbook:CHIN1404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4236
	Value Node: handbook:DENT4236
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6857
	Value Node: handbook:DENT6857
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEM2005
	Value Node: handbook:CHEM2005
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN2406
	Value Node: handbook:GRMN2406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4202
	Value Node: handbook:PODI4202
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:BMEG4552
	Value Node: handbook:BMEG4552
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5522
	Value Node: handbook:ACCT5522
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC3588
	Value Node: handbook:MUSC3588
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN3410
	Value Node: handbook:GRMN3410
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SCIE5519
	Value Node: handbook:SCIE5519
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6830
	Value Node: handbook:DENT6830
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INDO1404
	Value Node: handbook:INDO1404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5406
	Value Node: handbook:DENT5406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ENSC3019
	Value Node: handbook:ENSC3019
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5411
	Value Node: handbook:RMED5411
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEM3105
	Value Node: handbook:CHEM3105
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN1404
	Value Node: handbook:GRMN1404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6888
	Value Node: handbook:DENT6888
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6833
	Value Node: handbook:DENT6833
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC1017
	Value Node: handbook:EDUC1017
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED5701
	Value Node: handbook:GMED5701
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS3002
	Value Node: handbook:PHYS3002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4228
	Value Node: handbook:PODI4228
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS3101
	Value Node: handbook:PHYS3101
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATH1722
	Value Node: handbook:MATH1722
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEM2104
	Value Node: handbook:CHEM2104
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6817
	Value Node: handbook:DENT6817
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PUBH5801
	Value Node: handbook:PUBH5801
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SCIE3304
	Value Node: handbook:SCIE3304
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN2406
	Value Node: handbook:CHIN2406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL2408
	Value Node: handbook:ITAL2408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5104
	Value Node: handbook:LAWS5104
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED4220
	Value Node: handbook:IMED4220
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC4632
	Value Node: handbook:MUSC4632
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5402
	Value Node: handbook:DENT5402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SMED5411
	Value Node: handbook:SMED5411
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:KORE3408
	Value Node: handbook:KORE3408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM5106
	Value Node: handbook:OPTM5106
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC9985
	Value Node: handbook:EDUC9985
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5585
	Value Node: handbook:PSYC5585
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5570
	Value Node: handbook:MGMT5570
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHCY5603
	Value Node: handbook:PHCY5603
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP5406
	Value Node: handbook:SWSP5406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED5802
	Value Node: handbook:GMED5802
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GENE4003
	Value Node: handbook:GENE4003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5704
	Value Node: handbook:ACCT5704
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ENVE4601
	Value Node: handbook:ENVE4601
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5511
	Value Node: handbook:PSYC5511
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LACH5511
	Value Node: handbook:LACH5511
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED5412
	Value Node: handbook:IMED5412
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHEM1001
	Value Node: handbook:CHEM1001
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6911
	Value Node: handbook:DENT6911
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INDO2405
	Value Node: handbook:INDO2405
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:IMED3999
	Value Node: handbook:IMED3999
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MINE5552
	Value Node: handbook:MINE5552
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6827
	Value Node: handbook:DENT6827
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6821
	Value Node: handbook:DENT6821
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATH4002
	Value Node: handbook:MATH4002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6863
	Value Node: handbook:DENT6863
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5471
	Value Node: handbook:EDUC5471
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6891
	Value Node: handbook:DENT6891
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MEDC5803
	Value Node: handbook:MEDC5803
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5447
	Value Node: handbook:DENT5447
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4218
	Value Node: handbook:DENT4218
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5550
	Value Node: handbook:PSYC5550
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS1002
	Value Node: handbook:PHYS1002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS5552
	Value Node: handbook:CITS5552
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INDO1406
	Value Node: handbook:INDO1406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4232
	Value Node: handbook:DENT4232
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6836
	Value Node: handbook:DENT6836
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM4108
	Value Node: handbook:OPTM4108
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EMPL5450
	Value Node: handbook:EMPL5450
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5509
	Value Node: handbook:EDUC5509
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP3004
	Value Node: handbook:SWSP3004
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC1742
	Value Node: handbook:MUSC1742
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FNSC5627
	Value Node: handbook:FNSC5627
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5322
	Value Node: handbook:RMED5322
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SWSP5633
	Value Node: handbook:SWSP5633
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN2405
	Value Node: handbook:CHIN2405
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5665
	Value Node: handbook:MGMT5665
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:INMT5526
	Value Node: handbook:INMT5526
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SPAN3406
	Value Node: handbook:SPAN3406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FNSC5628
	Value Node: handbook:FNSC5628
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT6794
	Value Node: handbook:MGMT6794
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHIL3003
	Value Node: handbook:PHIL3003
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN3408
	Value Node: handbook:CHIN3408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5323
	Value Node: handbook:DENT5323
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5970
	Value Node: handbook:MGMT5970
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4213
	Value Node: handbook:PODI4213
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5209
	Value Node: handbook:LAWS5209
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6895
	Value Node: handbook:DENT6895
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6881
	Value Node: handbook:DENT6881
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6893
	Value Node: handbook:DENT6893
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6841
	Value Node: handbook:DENT6841
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:KORE3406
	Value Node: handbook:KORE3406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:RMED5801
	Value Node: handbook:RMED5801
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4123
	Value Node: handbook:DENT4123
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MATH1013
	Value Node: handbook:MATH1013
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS5105
	Value Node: handbook:LAWS5105
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYX1030
	Value Node: handbook:PHYX1030
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM5105
	Value Node: handbook:OPTM5105
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PUBH5721
	Value Node: handbook:PUBH5721
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4217
	Value Node: handbook:DENT4217
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5602
	Value Node: handbook:FINA5602
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6862
	Value Node: handbook:DENT6862
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARCT5502
	Value Node: handbook:ARCT5502
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CLAN2202
	Value Node: handbook:CLAN2202
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARCT5518
	Value Node: handbook:ARCT5518
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5532
	Value Node: handbook:ACCT5532
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC5832
	Value Node: handbook:PSYC5832
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS4110
	Value Node: handbook:LAWS4110
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC4141
	Value Node: handbook:MUSC4141
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6873
	Value Node: handbook:DENT6873
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CHIN1402
	Value Node: handbook:CHIN1402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:JAPN1404
	Value Node: handbook:JAPN1404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GRMN3407
	Value Node: handbook:GRMN3407
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT4122
	Value Node: handbook:DENT4122
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM5203
	Value Node: handbook:OPTM5203
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5407
	Value Node: handbook:DENT5407
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5444
	Value Node: handbook:DENT5444
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI4112
	Value Node: handbook:PODI4112
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ITAL1404
	Value Node: handbook:ITAL1404
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:LAWS4510
	Value Node: handbook:LAWS4510
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT5446
	Value Node: handbook:DENT5446
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MUSC1342
	Value Node: handbook:MUSC1342
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN3408
	Value Node: handbook:FREN3408
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ACCT5511
	Value Node: handbook:ACCT5511
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PODI5515
	Value Node: handbook:PODI5515
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:POLS5504
	Value Node: handbook:POLS5504
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:CITS1001
	Value Node: handbook:CITS1001
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PHYS5046
	Value Node: handbook:PHYS5046
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:GMED5801
	Value Node: handbook:GMED5801
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:DENT6865
	Value Node: handbook:DENT6865
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FINA5601
	Value Node: handbook:FINA5601
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5928
	Value Node: handbook:MGMT5928
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:OPTM4107
	Value Node: handbook:OPTM4107
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EMED5505
	Value Node: handbook:EMED5505
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MGMT5616
	Value Node: handbook:MGMT5616
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:EDUC5505
	Value Node: handbook:EDUC5505
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:STAT3402
	Value Node: handbook:STAT3402
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SMED5321
	Value Node: handbook:SMED5321
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:MSCI4006
	Value Node: handbook:MSCI4006
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:SSEH2295
	Value Node: handbook:SSEH2295
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:FREN1406
	Value Node: handbook:FREN1406
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:AUTO3002
	Value Node: handbook:AUTO3002
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PATH5122
	Value Node: handbook:PATH5122
	Source Constraint: [ shacl:message Literal("The prerequisite unit's level should be less than the unit's level.") ; shacl:select Literal("
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
                    ") ]
	Message: The prerequisite unit's level should be less than the unit's level.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:ARTF3050
	Value Node: handbook:ARTF3050
	Source Constraint: [ shacl:message Literal("A unit cannot be its own prerequisite.") ; shacl:select Literal("
						PREFIX h: <http://university.org/>
						SELECT $this 
						WHERE {
							$this h:has_prerequisite $this .
						}
					") ]
	Message: A unit cannot be its own prerequisite.
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: shacl:Violation
	Source Shape: h:unit_shape
	Focus Node: handbook:PSYC2208
	Value Node: handbook:PSYC2208
	Source Constraint: [ shacl:message Literal("A unit cannot be its own prerequisite.") ; shacl:select Literal("
						PREFIX h: <http://university.org/>
						SELECT $this 
						WHERE {
							$this h:has_prerequisite $this .
						}
					") ]
	Message: A unit cannot be its own prerequisite.

