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

% Forward Chaining Implementation
% In Prolog, forward chaining can be simulated by asserting derived facts.

% Define a predicate to perform forward chaining.
forward_chaining :-
    new_fact(P),  % Find a new fact
    !,
    write('Derived: '), write(P), nl,
    assert(P),    % Add it to the knowledge base
    forward_chaining.  % Continue forward chaining

forward_chaining.

% Define a predicate to find new facts based on existing rules.
new_fact(disease(X, Disease)) :-
    disease(X, Disease),
    \+ disease(X, Disease).  % Disease not already known

% Start forward chaining to derive conclusions.
?- forward_chaining.
