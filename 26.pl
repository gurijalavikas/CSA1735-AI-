% Facts: fruit_color(Fruit, Color).
fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(grape, green).
fruit_color(orange, orange).
fruit_color(lemon, yellow).
fruit_color(strawberry, red).

% Rule to find the color of a given fruit using backtracking.
find_fruit_color(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Query to find all colors of a given fruit.
list_all_colors(Fruit) :-
    find_fruit_color(Fruit, Color),
    format('The color of ~w is ~w.~n', [Fruit, Color]),
    fail.
list_all_colors(_).  % This ensures the query succeeds even after all possibilities are exhausted.
