# a function which takes in a string describing a unit assessment,
# returns a list of assessment categories which were mentioned in the string
assessment_categories = ["assignment", 
                        "report", 
                        "quiz", 
                        "presentation", 
                        "exam", 
                        "seminar", 
                        "practical", 
                        "activity", 
                        "debate", 
                        "paper", 
                        "research_proposal", 
                        "review", 
                        "essay", 
                        "test"]

def determine_assessments(assessment_string):
    assessment = assessment_string.lower()
    category_matches = []
    for category in assessment_categories:
        if category in assessment:
            category_matches.append(category)
    return category_matches
    
# still need to check what outliers we have
# can do this by printing out the string if it gets no matches