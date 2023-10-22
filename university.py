"""
David Wang (23064035)
Hannah Doret (22846377)
"""

from rdflib import Graph, Literal, RDFS
from rdflib.namespace import RDF, Namespace
from assessments import determine_assessments
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
h = Namespace("http://university.org/")

g.bind("handbook", h)

#Create classes
unit = h.unit
school = h.school
board_of_examiners = h.board_of_examiners
delivery_mode = h.delivery_mode
level = h.level
credit = h.credit
assessment = h.assessment
# prerequisite = h.prerequisite
# advisable_prior_study = h.advisable_prior_study
major = h.major
course = h.course

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
g.add((assessment, RDF.type, RDFS.Class))
g.add((assessment, RDFS.label, Literal("Assessment")))
g.add((major, RDF.type, RDFS.Class))
g.add((major, RDFS.label, Literal("Major")))
g.add((course, RDF.type, RDFS.Class))
g.add((course, RDFS.label, Literal("Course")))

# Create specific assessment objects
participation = h.participation
group = h.group
practical = h.practical
oral = h.oral
written = h.written
multimedia = h.multimedia
project = h.project
exam = h.exam
test = h.test
misc = h.misc

# Add assessment objects (type = assessment class)
g.add((participation, RDF.type, assessment))
g.add((group, RDF.type, assessment)) 
g.add((practical, RDF.type, assessment)) 
g.add((oral, RDF.type, assessment)) 
g.add((written, RDF.type, assessment)) 
g.add((multimedia, RDF.type, assessment)) 
g.add((project, RDF.type, assessment)) 
g.add((exam, RDF.type, assessment)) 
g.add((test, RDF.type, assessment)) 
g.add((misc, RDF.type, assessment))

#Create relations
has_title = h.has_title
has_school = h.has_school
has_board_of_examiners = h.has_board_of_examiners
has_unit_delivery_mode = h.has_unit_delivery_mode
has_level = h.has_level
has_description = h.has_description
has_credit = h.has_credit
has_outcome = h.has_outcome
has_assessment = h.has_assessment
has_prerequisite = h.has_prerequisite
has_advisable_prior_study = h.has_advisible_prior_study
has_note = h.has_note
major_of_courses = h.major_of_courses
has_unit = h.has_unit
has_bridging = h.has_bridging
has_major = h.has_major
has_name = h.has_name # used for assessment object names eg. "exam"
has_number = h.has_number # used to give level objects an integer literal, bc integers are easier to use in SHACL
has_contact_hrs = h.has_contact_hrs

#Add relations
g.add((has_title, RDF.type, RDF.Property))
g.add((has_school, RDF.type, RDF.Property))
g.add((has_board_of_examiners, RDF.type, RDF.Property))
g.add((has_unit_delivery_mode, RDF.type, RDF.Property))
g.add((has_level, RDF.type, RDF.Property))
g.add((has_description, RDF.type, RDF.Property))
g.add((has_credit, RDF.type, RDF.Property))
g.add((has_outcome, RDF.type, RDF.Property))
g.add((has_assessment, RDF.type, RDF.Property))
g.add((has_prerequisite, RDF.type, RDF.Property))
g.add((has_advisable_prior_study, RDF.type, RDF.Property))
g.add((has_note, RDF.type, RDF.Property))
g.add((major_of_courses, RDF.type, RDF.Property))
g.add((has_unit, RDF.type, RDF.Property))
g.add((has_bridging, RDF.type, RDF.Property))
g.add((has_major, RDF.type, RDF.Property))
g.add((has_name, RDF.type, RDF.Property))
g.add((has_number, RDF.type, RDF.Property))
g.add((has_contact_hrs, RDF.type, RDF.Property))

#Use Json object to add to graph
for unit_name in units_data:
    #Define URI
    unit_code = h[unit_name]
    unit_school = h[units_data[unit_name]["school"].replace(" ", "_")]
    unit_board_of_examiners = h[units_data[unit_name]["board_of_examiners"].replace(" ", "_")]
    unit_delivery_mode = h[units_data[unit_name]["delivery_mode"].replace(" ", "_")]
    unit_level = h[units_data[unit_name]["level"].replace(" ", "_")]
    unit_credit = h[units_data[unit_name]["credit"].replace(" ", "_")]

    #Name
    g.add((unit_code, RDF.type, unit))
    g.add((unit_code, RDFS.label, Literal(unit_name)))
    
    #Title
    g.add((unit_code, has_title, Literal(units_data[unit_name]["title"])))
    
    #School
    g.add((unit_school, RDF.type, school))
    g.add((unit_school, RDFS.label, Literal(units_data[unit_name]["school"])))
    g.add((unit_code, has_school, unit_school))
    
    #Board of Examiners
    if units_data[unit_name]["board_of_examiners"] != "" and units_data[unit_name]["board_of_examiners"] != "NA":
        g.add((unit_board_of_examiners, RDF.type, board_of_examiners))
        g.add((unit_board_of_examiners, RDFS.label, Literal(units_data[unit_name]["board_of_examiners"])))
        g.add((unit_code, has_board_of_examiners, unit_board_of_examiners))
    
    #Delivery mode
    g.add((unit_delivery_mode, RDF.type, delivery_mode))
    g.add((unit_delivery_mode, RDFS.label, Literal(units_data[unit_name]["delivery_mode"])))
    g.add((unit_code, has_unit_delivery_mode, unit_delivery_mode))
    
    #Level
    g.add((unit_level, RDF.type, level))
    g.add((unit_level, has_number, Literal(int(units_data[unit_name]["level"]))))
    g.add((unit_code, has_level, unit_level))
    
    #Description
    g.add((unit_code, has_description, Literal(units_data[unit_name]["description"])))
    
    #Credit
    g.add((unit_credit, RDF.type, credit))
    g.add((unit_credit, RDFS.label, Literal(units_data[unit_name]["credit"])))
    g.add((unit_code, has_credit, unit_credit))
    
    #Assessments
    assessments = []
    for assessment_item in units_data[unit_name]["assessment"]:
        these_assessments = determine_assessments(assessment_item)
        # add assessments we found to the assessments list, without duplicates (do we want duplicates??? eg. if 2 of the strings mentioned reports)
        for assessment in these_assessments:
            if assessment not in assessments:
                assessments.append(assessment)
    for a in assessments:
        # refer to the URI we already created for this type of assessment, and add relation to it
        assessment_object = h[a]
        g.add((unit_code, has_assessment, assessment_object))

    #Outcomes
    if units_data[unit_name].get("outcomes") != None:
        for unit_outcome in units_data[unit_name]["outcomes"]:
            g.add((unit_code, has_outcome, Literal(unit_outcome)))
    
    #Prerequisites
    if units_data[unit_name].get("prerequisites_cnf") != None:
        full_prerequisite = []
        for prerequisite_thing in units_data[unit_name]["prerequisites_cnf"]:
            for prereq in prerequisite_thing:
                full_prerequisite.append(prereq)
        for prerequisite_item in full_prerequisite:
            g.add((unit_code, has_prerequisite, h[prerequisite_item.replace(" ", "_")]))

    #Advisable Prior Study
    if units_data[unit_name].get("advisable_prior_study") != None:
        for advisable_item in units_data[unit_name]["advisable_prior_study"]:
            g.add((unit_code, has_advisable_prior_study, h[advisable_item.replace(" ", "_")]))

    #Contact hours
    if units_data[unit_name].get("contact") != None:
        hours = 0
        for contact_item in units_data[unit_name]["contact"]:
            hours += int(units_data[unit_name]["contact"][contact_item])
        g.add((unit_code, has_contact_hrs, Literal(int(hours))))

    #Note
    if units_data[unit_name].get("note") != None:
        g.add((unit_code, has_note, Literal(units_data[unit_name]["note"])))

#Add majors data
for major_name in majors_data:
    major_code = h[major_name]
    g.add((major_code, RDF.type, major))
    g.add((major_code, RDFS.label, Literal(major_name)))
    g.add((major_code, has_title, Literal(majors_data[major_name]["title"])))
    g.add((major_code, has_description, Literal(majors_data[major_name]["description"])))

    for this_course in majors_data[major_name]["courses"]:
        major_course = h[this_course]
        g.add((major_course, RDF.type, course))
        g.add((major_code, major_of_courses, major_course))

    major_school = h[majors_data[major_name]["school"].replace(" ", "_")]
    g.add((major_school, RDF.type, school))
    g.add((major_school, RDFS.label, Literal(majors_data[major_name]["school"])))
    g.add((major_code, has_school, major_school))

    for bridging_unit in majors_data[major_name]["bridging"]:
        unit_code = h[bridging_unit]
        g.add((unit_code, RDF.type, unit))
        g.add((major_code, has_bridging, unit_code))

    for taught_unit in majors_data[major_name]["units"]:
        unit_code = h[taught_unit]
        g.add((unit_code, RDF.type, unit))
        g.add((major_code, has_unit, unit_code))
        g.add((unit_code, has_major, major_code))

    if majors_data[major_name].get("outcomes") != None:
        for major_outcome in majors_data[major_name]["outcomes"]:
            g.add((major_code, has_outcome, Literal(major_outcome)))


# print graph
g.serialize(destination = "handbook.ttl", format='ttl', indent=4)