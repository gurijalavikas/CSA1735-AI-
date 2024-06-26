% Facts: bird(Name, CanFly).
bird(sparrow, can_fly).
bird(penguin, cannot_fly).
bird(eagle, can_fly).
bird(ostrich, cannot_fly).
bird(swallow, can_fly).
bird(kiwi, cannot_fly).
bird(albatross, can_fly).

% Rule to determine if a particular bird can fly.
can_bird_fly(Name, can_fly) :-
    bird(Name, can_fly), !.

can_bird_fly(Name, cannot_fly) :-
    bird(Name, cannot_fly), !.

% Queries to determine if a particular bird can fly or not.
can_bird_fly_query(Name) :-
    can_bird_fly(Name, can_fly),
    format('The bird ~w can fly.~n', [Name]).

can_bird_fly_query(Name) :-
    can_bird_fly(Name, cannot_fly),
    format('The bird ~w cannot fly.~n', [Name]).

% Catch-all for birds not in the database.
can_bird_fly_query(Name) :-
    \+ bird(Name, _),
    format('The bird ~w is not in the database.~n', [Name]).
