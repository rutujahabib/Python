#nesting 
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lyon", "Marseille"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Munich", "Hamburg"],"total_visits": 5},  
}

travel_log = {
    {
        "country":"France", 
        "cities_visited": ["Paris", "Lyon", "Marseille"], 
        "total_visits": 12},
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Munich", "Hamburg"],
        "total_visits": 5},  
}

