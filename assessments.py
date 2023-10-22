# 1 category != 1 assessment
# one assessment may fit into multiple categories
# also, one assessment string may describe multiple assessments
# so we can't really tell exactly how many assessments a unit has
# we can only list the types of assessments it has 

# assessment categories: participation, group, practical, oral, written, multimedia, project, exam, test, misc
assessment_dictionary = {
    "participation":    ["participation",
                        "particpation",
                        "partipation",
                        "participatiton",
                        "engagement", 
                        "contribution", 
                        "attendance", 
                        "behaviour",
                        "conduct",
                        "effort",
                        "communication"],
    
    "group":            ["group",
                        "team"],
    
    "practical":        ["practical", 
                        "activity", 
                        "activities", 
                        "lab", 
                        "workshop", 
                        "tutorial", 
                        "exercise", 
                        "training", 
                        "placement", 
                        "log", 
                        "portfolio",
                        "feedback",
                        "rating",
                        "performance"],
    
    "oral":             ["oral", 
                        "presentation", 
                        "seminar", 
                        "debate", 
                        "discussion", 
                        "role-play", 
                        "interview"],
    
    "written":          ["written", 
                        "writing", 
                        "report", 
                        "review", 
                        "essay", 
                        "paper", 
                        "research proposal", 
                        "journal", 
                        "analysis", 
                        "analyses", 
                        "case study", 
                        "reflection", 
                        "article", 
                        "blog", 
                        "bibliography", 
                        "dissertation", 
                        "notebook", 
                        "glossary", 
                        "document", 
                        "critique",
                        "op-ed",
                        "memorandum",
                        "diary",
                        "exegesis",
                        "letter",
                        "short answer",
                        "thesis",
                        "manuscript",
                        "case study"],
    
    "multimedia":       ["video", 
                        "podcast",
                        "poster"],
    
    "project":          ["project", 
                        "assignment", 
                        "research"],
    
    "exam":             ["exam",
                        "OSCE"],
    
    "test":             ["test", 
                        "quiz", 
                        "mid-semester"],

                        # keywords I do not know how to categorize:
    "misc":             ["assessment",
                        "plan",
                        "home work",
                        "evaluation",
                        "design",
                        "moot",
                        "composition",
                        "translation",
                        "reading",
                        "response",
                        "commentary",
                        "interpreting",
                        "methodolgy",
                        "survey",
                        "map",
                        "drawing",
                        "fair",
                        "learning",
                        "narrative",
                        "framework",
                        "brief",
                        "challenge",
                        "walk",
                        "object history",
                        "task",
                        "story",
                        "work",
                        "memo",
                        "problem",
                        "statement",
                        "preparation",
                        "application",
                        "note",
                        "edit",
                        "proposal",
                        "profile",
                        "piece",
                        "simulation",
                        "log",
                        "collection",
                        "worksheet",
                        "submission"]
}

# a function which takes in a string describing a unit assessment,
# returns a list of assessment categories which were mentioned in the string
def determine_assessments(assessment_string):
    assessment = assessment_string.lower()
    category_matches = []

    for category in assessment_dictionary:
        for keyword in assessment_dictionary[category]:
            if keyword in assessment:
                category_matches.append(category)

    return category_matches