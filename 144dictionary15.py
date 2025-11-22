# Nested dictionary
myfamily = {
    "child1": {"name": "Haley", "year": "2004"},
    "child2": {"name": "Alex", "year": "2007"},
    "child3": {"name": "Luke", "year": "2011"}
}
print(myfamily)
print(myfamily["child2"])
print(myfamily["child2"]["name"])
print(myfamily["child2"].items())