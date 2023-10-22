from owlready2 import get_ontology, Thing, ObjectProperty, DataProperty
import json
from assessments import determine_assessments

onto = get_ontology("http://university.org/")

#Open and parse json objects
with open('units.json', 'r') as units:
    units_data = json.load(units)
units.close()

with open('majors.json', 'r') as majors:
    majors_data = json.load(majors)
majors.close()

with onto:
    #Define Classes
    class Unit(Thing): pass
    class School(Thing): pass
    class BoardofExaminers(Thing): pass
    class DeliveryMode(Thing): pass
    class Assessment(Thing): pass
    class Major(Thing): pass
    class Course(Thing): pass
    
    #Define assessments
    assessments = ["Participation", "Group", "Practical", "Oral", "Written", "Multimedia", "Project", "Exam", "Test", "Misc"]
    for assessment in assessments:
        exec(f"class {assessment}(Assessment): pass")
    
    #define relations
    class has_title(Unit >> str, DataProperty): pass
    class has_school(Unit >> School): pass
    class has_board_of_examiners(Unit >> BoardofExaminers): pass
    class has_unit_delivery_mode(Unit >> DeliveryMode): pass
    class has_level(Unit >> int, DataProperty): pass
    class has_description(Unit >> str, DataProperty): pass
    class has_credit(Unit >> int, DataProperty):pass
    class has_outcome(Unit >> str, DataProperty): pass
    class has_assessment(Unit >> Assessment): pass
    class has_prerequisite(Unit >> Unit): pass
    class has_advisable_prior_study(Unit >> Unit): pass
    class has_note(Unit >> str): pass
    class major_of_courses(Major >> Course): pass
    class has_unit(Major >> Unit): pass
    class has_bridging(Major >> Unit): pass

    #inverse property
    class has_major(ObjectProperty):
        domain              = [Unit]
        range               = [Major]
        inverse_property    = has_unit

    class has_contact(Unit >> int): pass
    #has_name = h.has_name # used for assessment object names eg. "exam"
    #has_number = h.has_number # used to give level objects an integer literal, bc integers are easier to use in SHACL

    # CITS3200 = Unit("CITS3200", has_title=[units_data["CITS3200"]['title']])
    data_stuff = []
    
    #Add unit information for every unit
    for unit_name in units_data:
        # if units_data[unit_name]["description"] not in data_stuff:
        #     data_stuff.append(units_data[unit_name]["description"])
        
        # Add school if it exists
        school_string = ""
        if units_data[unit_name]["school"] != "":
            school_string = f'has_school=[School("{units_data[unit_name]["school"]}")],'
        
        # Add board of examiner if it exists
        board_of_examiners_string = ""
        if units_data[unit_name]["board_of_examiners"] != "" and units_data[unit_name]["board_of_examiners"] != "NA":
            board_of_examiners_string = f'has_board_of_examiners=[BoardofExaminers("{units_data[unit_name]["board_of_examiners"]}")],'

        # Add delivery mode if it exists
        delivery_string = ""
        if units_data[unit_name]["delivery_mode"] != "":
            delivery_string = f'has_unit_delivery_mode=[DeliveryMode("{units_data[unit_name]["delivery_mode"]}")],'

        # Add all outcomes if it exists
        if units_data[unit_name].get("outcomes") != None:
            if units_data[unit_name]["outcomes"]:
                outcome_string = f'has_outcome={units_data[unit_name]["outcomes"]},'

        # Add all assessments if it exists
        if units_data[unit_name].get("assessment") != None:
            if units_data[unit_name]["assessment"] and "" not in units_data[unit_name]["assessment"] and " " not in units_data[unit_name]["assessment"]:
                assessments = []
                for assessment_item in units_data[unit_name]["assessment"]:
                    these_assessments = determine_assessments(assessment_item)
                    for assessment in these_assessments:
                        if assessment not in assessments:
                            assessments.append(assessment)
                i = 0
                assessment_string = 'has_assessment=['
                for (i, assessment) in enumerate(assessments):
                    if i != len(assessments) - 1:
                        assessment_string += f'Assessment("{assessment}"), '
                    else:
                        assessment_string += f'Assessment("{assessment}")],'

        # Add all prerequisites if it exists
        if units_data[unit_name].get("prerequisites_cnf") != None:
            if units_data[unit_name]["prerequisites_cnf"]:
                full_prerequisite = []
                for prerequisite_thing in units_data[unit_name]["prerequisites_cnf"]:
                    for prereq in prerequisite_thing:
                        full_prerequisite.append(prereq)
                # print(full_prerequisite)
                i = 0
                prerequisite_string = 'has_prerequisite=['
                for (i, prereq) in enumerate(full_prerequisite):
                    if i != len(full_prerequisite) - 1:
                        prerequisite_string += f'Unit("{prereq}"), '
                    else:
                        prerequisite_string += f'Unit("{prereq}")],'
                # print(prerequisite_string)
        
        #Add advisable prior study if it exists
        if units_data[unit_name].get("advisable_prior_study") != None:
            if units_data[unit_name]["advisable_prior_study"]:
                i = 0
                advisable_string = 'has_advisable_prior_study=['
                for (i, advisable) in enumerate(units_data[unit_name]["advisable_prior_study"]):
                    if i != len(units_data[unit_name]["advisable_prior_study"]) - 1:
                        advisable_string += f'Unit("{advisable}"), '
                    else:
                        advisable_string += f'Unit("{advisable}")],'
        
        #Add contact hours if it exists
        if units_data[unit_name].get("contact") != None:
            if units_data[unit_name]["contact"]:
                hours = 0
                for contact_item in units_data[unit_name]["contact"]:
                    hours += int(units_data[unit_name]["contact"][contact_item])
                contact_string = f'has_contact=[{hours}],'
        
        #Add notes if it exists
        note_string = ""
        if units_data[unit_name].get("note") != None:
            note_string = f'has_note=["{units_data[unit_name]["note"]}"],'
        
        # Add all information to each unit
        unit_add = f'''{unit_name} = \
            Unit("{unit_name}", 
                has_title=["{units_data[unit_name]["title"]}"], 
                {school_string}
                {board_of_examiners_string}
                {delivery_string}
                has_level=[{int(units_data[unit_name]["level"])}],
                has_description=["""{units_data[unit_name]["description"].replace('"', '')}"""],
                has_credit=[{int(units_data[unit_name]["credit"])}],
                {outcome_string}
                {assessment_string}
                {prerequisite_string}
                {advisable_string}
                {contact_string}
                {note_string}
            )
        '''
        # print(unit_add)
        exec(unit_add)
        # AGRI5403 = Unit('AGRI5403', has_title=['Advanced Commodity Marketing'], has_school=[School('Agriculture and Environment')]) 
    # print(data_stuff[0])
    onto.save(file = "handbook.owl", format = "rdfxml")