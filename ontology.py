from owlready2 import get_ontology, Thing, ObjectProperty, DataProperty, close_world, sync_reasoner_hermit
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
    class has_course(Major >> Course): pass
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

    data_stuff = []
    #Add unit to to ontology
    for unit_name in units_data:
        # Add school if it exists
        unit_school_string = ""
        if units_data[unit_name]["school"] != "":
            unit_school_string = f'has_school=[School("{units_data[unit_name]["school"]}")],'
        
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
                unit_outcome_string = f'has_outcome={units_data[unit_name]["outcomes"]},'

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
                {unit_school_string}
                {board_of_examiners_string}
                {delivery_string}
                has_level=[{int(units_data[unit_name]["level"])}],
                has_description=["""{units_data[unit_name]["description"].replace('"', '')}"""],
                has_credit=[{int(units_data[unit_name]["credit"])}],
                {unit_outcome_string}
                {assessment_string}
                {prerequisite_string}
                {advisable_string}
                {contact_string}
                {note_string}
            )
        '''
        # print(unit_add)
        exec(unit_add)
    
    #Add majors to ontology
    for major_name in majors_data:
        
        # Add school if it exists
        major_school_string = ""
        if majors_data[major_name]["school"] != "":
            major_school_string = f'has_school=[School("{majors_data[major_name]["school"]}")],'
        
        # Add all outcomes if it exists
        if majors_data[major_name].get("outcomes") != None:
            if majors_data[major_name]["outcomes"]:
                major_outcome_string = f'has_outcome={majors_data[major_name]["outcomes"]},'
        
        # Add all courses
        course_string = 'has_course=['
        for (i, course) in enumerate(majors_data[major_name]["courses"]):
            if i != len(majors_data[major_name]["courses"]) - 1:
                course_string += f'Course("{course}"), '
            else:
                course_string += f'Course("{course}")],'
        
        # Add all bridging units
        if majors_data[major_name]["bridging"]:
            bridging_string = 'has_bridging=['
            for (i, bridging) in enumerate(majors_data[major_name]["bridging"]):
                if i != len(majors_data[major_name]["bridging"]) - 1:
                    bridging_string += f'Unit("{bridging}"), '
                else:
                    bridging_string += f'Unit("{bridging}")],'

        # Add all units
        unit_string = 'has_unit=['
        for (i, unit) in enumerate(majors_data[major_name]["units"]):
            if i != len(majors_data[major_name]["units"]) - 1:
                unit_string += f'Unit("{unit}"), '
            else:
                unit_string += f'Unit("{unit}")],'
        
        # Add all information to each major
        major_add = f'''{major_name.replace("-", "_")} = \
            Major("{major_name}", 
                has_title=["{majors_data[major_name]["title"]}"], 
                {major_school_string}
                has_description=["""{majors_data[major_name]["description"].replace('"', '')}"""],
                {major_outcome_string}
                {course_string}
                {unit_string}
                {bridging_string}
            )
        '''
        exec(major_add)
close_world(Unit)
sync_reasoner_hermit(infer_property_values = True)

onto.save(file = "handbook.owl", format = "rdfxml")