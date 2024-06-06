def relations_Luke(member):
    relations = {"DarthVader" : "Father", "Leah" : "Sister", "Han" : "Brother-in-law"}
    relation = relations.get(member)
    print("Luke, I am your " + str(relation))

relations_Luke("Leah")