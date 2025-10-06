destinations=["Paris, France","Shanghai, China","Los Angeles, USA","Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destiantion_index(destination):
    for item in range(len(destinations)):
        if(destinations[item]==destination):
            destination_index=item
    return destination_index
def get_traveler_location(traveler):
    traveler_destination=traveler[1]
    traveler_destination_index=get_destiantion_index(traveler_destination)
    return traveler_destination_index

attractions=[[] for destination in destinations]

def add_attraction(destination,attraction):
    destination_index=get_destiantion_index(destination)
    attractions_for_destination=attractions[destination_index]
    attractions_for_destination.append(attraction)
    return attractions_for_destination


add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


print(get_destiantion_index("Los Angeles, USA"))
print(get_destiantion_index("Paris, France"))
test_destination_index=get_traveler_location(test_traveler)
print(test_destination_index)
print(attractions)

def find_attractions(destination,interests):
    destination_index=get_destiantion_index(destination)
    attractions_in_city=attractions[destination_index]
    attractions_with_interest=[]
    for attraction in attractions_in_city:
        possible_attraction=attraction
        attraction_tags=attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
                break

    return attractions_with_interest



la_arts=find_attractions("Los Angeles, USA",['art'])
print(la_arts)