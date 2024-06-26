% Facts
symptom(john, fever).
symptom(john, cough).
symptom(john, sore_throat).

% Rules
disease(X, flu) :-
    symptom(X, fever),
    symptom(X, cough).

disease(X, strep_throat) :-
    symptom(X, fever),
    symptom(X, sore_throat).

disease(X, common_cold) :-
    symptom(X, cough),
    symptom(X, sore_throat).

% Backward Chaining Implementation
% In Prolog, we can use recursive predicates to simulate backward chaining.

% Define a predicate to perform backward chaining.
backward_chaining(Goal) :-
    Goal,
    write('Goal '), write(Goal), write(' is satisfied.'), nl.

% Define rules to satisfy the goal based on symptoms and diseases.
disease(X, Disease) :-
    symptom(X, Symptom),
    backward_chaining(symptom(X, Symptom)),
    disease(X, Disease).

% Query to diagnose diseases for 'john'.
?- disease(john, Disease).
