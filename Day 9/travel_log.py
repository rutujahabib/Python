#dictionaries in lists

travel_log = [
    {
        "country":"France", 
        "cities_visited": ["Paris", "Lyon", "Marseille"], 
        "total_visits": 12},
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Munich", "Hamburg"],
        "total_visits": 5},
]

def add_new_country(countries, cities, visits):
    new_country = {} 
    new_country['country'] = countries
    new_country['cities_visited'] = cities
    new_country['total_viists'] = visits
    travel_log.append(new_country)

add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)    
print(travel_log)