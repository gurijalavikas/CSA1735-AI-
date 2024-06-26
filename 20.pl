% Facts: planet(Name, Type, DistanceFromSun, NumberOfMoons).
planet('Mercury', terrestrial, 57.91, 0).
planet('Venus', terrestrial, 108.2, 0).
planet('Earth', terrestrial, 149.6, 1).
planet('Mars', terrestrial, 227.9, 2).
planet('Jupiter', gas_giant, 778.5, 79).
planet('Saturn', gas_giant, 1434, 82).
planet('Uranus', ice_giant, 2871, 27).
planet('Neptune', ice_giant, 4495, 14).

% Rule to find the type of a planet.
find_type(Name, Type) :-
    planet(Name, Type, _, _).

% Rule to find the distance of a planet from the sun.
find_distance(Name, Distance) :-
    planet(Name, _, Distance, _).

% Rule to find the number of moons of a planet.
find_moons(Name, Moons) :-
    planet(Name, _, _, Moons).

% Rule to find all planets of a given type.
find_planets_by_type(Type, Name) :-
    planet(Name, Type, _, _).

% Rule to find planets within a certain distance from the sun.
find_planets_within_distance(MaxDistance, Name) :-
    planet(Name, _, Distance, _),
    Distance =< MaxDistance.
