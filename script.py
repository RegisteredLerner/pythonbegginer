destinations=["Paris, France","Shanghai, China","Los Angeles, USA","Sao Paulo, Brazil,", "Cairo, Egypt"]
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





print(get_destiantion_index("Los Angeles, USA"))
print(get_destiantion_index("Paris, France"))
test_destination_index=get_traveler_location(test_traveler)
print(test_destination_index)