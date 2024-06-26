import itertools

def calculate_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** 0.5

def total_distance(permutation, distance_matrix):
    distance = 0
    num_cities = len(permutation)
    for i in range(num_cities - 1):
        distance += distance_matrix[permutation[i]][permutation[i + 1]]
    distance += distance_matrix[permutation[-1]][permutation[0]]  # Return to start
    return distance

def travelling_salesman_problem(cities):
    num_cities = len(cities)
    distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]
    
    min_distance = float('inf')
    best_permutation = None
    
    for permutation in itertools.permutations(range(num_cities)):
        current_distance = total_distance(permutation, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_permutation = permutation
    
    return best_permutation, min_distance


cities = [
    (0, 0),
    (1, 3),
    (4, 3),
    (6, 1)
]

best_route, min_distance = travelling_salesman_problem(cities)
print(f"Best route: {best_route}")
print(f"Minimum distance: {min_distance:.2f}")
