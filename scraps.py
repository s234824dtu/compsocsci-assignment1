
# for many researcher names there are multiple results. to disambiguate we check against their their listed institutions on the organization page and the known institutions and research subject from openalex
#social_concepts = ["Sociology", "Psychology", "Economics", "Political Science"]
#quant_concepts = ["Mathematics", "Physics", "Computer Science"]
#def disambig(i):
#    _, known_institution, alex_researcher_info = alex_info[i]
#    if (len(alex_researcher_info) == 1):
#        print("no ambig")
#        return alex_info[0]
#    if not known_institution is None:
#        known_institutions_components = re.split(r',|')
#        search_results = pyalex.Institutions().search(known_institution).get()
#        if len(search_results) > 1:
#            known_institution_id = search_results[0]["id"]
#            for potential_researcher_info in alex_researcher_info:
#                if any([affiliation["institution"]["id"] in known_institution_id
#                                        for affiliation
#                                        in potential_researcher_info["affiliations"]]):
#                    print("affiliation found")
#                    return potential_researcher_info
#    correct_subject_researchers = []
#    for potential_researcher_info in alex_researcher_info:
#        researcher_concepts = [concept["display_name"]
#                                   for concept
#                                   in potential_researcher_info["x_concepts"]]
#        social_found = any([(social_concept in researcher_concepts) for social_concept in social_concepts])
#        quant_found = any([(quant_concept in researcher_concepts) for quant_concept in quant_concepts])
#        print(social_found, quant_found)
#        if social_found or quant_found: 
#            print(potential_researcher_info["x_concepts"])
#        if social_found and quant_found:
#            correct_subject_researchers.append(potential_researcher_info)
#            print("correct subject researcher found")
#    if len(correct_subject_researchers) == 1:
#        return correct_subject_researchers[0] 
#    print(alex_researcher_info)
#    return None
#