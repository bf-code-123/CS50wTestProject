#nest data structure within each other
#list of dictionaries, where each person has diff properties
people = [
    {"name": "Harry", "house": "Gryf"},
    {"name": "Cho", "house": "Raven"},
    {"name": "Draco", "house": "Slyth"},
]

#if you change name to house, then order changes
#def f(person):
#    return person["name"]

#sort then print people
#the way to sort people is running function
#people.sort(key=f)

#lambda shortens so you dont have to write a separate function
people.sort(key=lambda person: person["name"])

print(people)