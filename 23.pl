% Facts: parent(Parent, Child).
parent(john, mary).
parent(john, james).
parent(susan, mary).
parent(susan, james).
parent(mary, susan_jr).
parent(mary, tom).
parent(peter, susan_jr).
parent(peter, tom).
parent(james, linda).
parent(james, mike).
parent(sara, linda).
parent(sara, mike).

% Rule to determine if X is a child of Y.
child(X, Y) :-
    parent(Y, X).

% Rule to determine if X is a sibling of Y.
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Rule to determine if X is a grandparent of Y.
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Rule to determine if X is a grandchild of Y.
grandchild(X, Y) :-
    grandparent(Y, X).

% Rule to determine if X is a cousin of Y.
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).

% Rule to determine if X is an uncle or aunt of Y.
uncle_or_aunt(X, Y) :-
    sibling(X, Z),
    parent(Z, Y).

% Rule to determine if X is a nephew or niece of Y.
nephew_or_niece(X, Y) :-
    uncle_or_aunt(Y, X).

% Rule to determine if X is a male.
male(john).
male(james).
male(peter).
male(tom).
male(mike).

% Rule to determine if X is a female.
female(susan).
female(mary).
female(susan_jr).
female(sara).
female(linda).

% Rule to determine if X is a father of Y.
father(X, Y) :-
    parent(X, Y),
    male(X).

% Rule to determine if X is a mother of Y.
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Rule to determine if X is a son of Y.
son(X, Y) :-
    child(X, Y),
    male(X).

% Rule to determine if X is a daughter of Y.
daughter(X, Y) :-
    child(X, Y),
    female(X).

% Rule to determine if X is a grandfather of Y.
grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

% Rule to determine if X is a grandmother of Y.
grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).
