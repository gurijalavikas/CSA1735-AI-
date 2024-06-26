% State Representation: state(MonkeyPosition, BoxPosition, MonkeyOnBox, HasBanana)
% MonkeyPosition: 'at_door', 'at_window', 'at_middle'
% BoxPosition: 'at_door', 'at_window', 'at_middle'
% MonkeyOnBox: 'on_floor', 'on_box'
% HasBanana: 'has_not', 'has'

% Initial State
initial_state(state(at_door, at_window, on_floor, has_not)).

% Goal State
goal_state(state(_, _, _, has)).

% Actions
move(state(Monkey, Box, on_floor, Banana), walk(Monkey, NewMonkey), state(NewMonkey, Box, on_floor, Banana)) :-
    Monkey \= NewMonkey.

move(state(at_door, Box, on_floor, Banana), push_box(at_door, NewPos), state(NewPos, NewPos, on_floor, Banana)) :-
    Box = at_door.

move(state(at_window, Box, on_floor, Banana), push_box(at_window, NewPos), state(NewPos, NewPos, on_floor, Banana)) :-
    Box = at_window.

move(state(at_middle, Box, on_floor, Banana), push_box(at_middle, NewPos), state(NewPos, NewPos, on_floor, Banana)) :-
    Box = at_middle.

move(state(Pos, Pos, on_floor, Banana), climb_box, state(Pos, Pos, on_box, Banana)).

move(state(Pos, Pos, on_box, has_not), grab_banana, state(Pos, Pos, on_box, has)).

% Solution Search
solve_problem :-
    initial_state(InitialState),
    goal_state(GoalState),
    plan(InitialState, GoalState, [], Plan),
    print_plan(Plan).

plan(State, State, Plan, Plan).

plan(State, GoalState, PartialPlan, Plan) :-
    move(State, Action, NewState),
    \+ member(NewState, PartialPlan),  % Avoid loops
    plan(NewState, GoalState, [Action|PartialPlan], Plan).

% Print Plan
print_plan([]).

print_plan([Action|Rest]) :-
    print_plan(Rest),
    write(Action), nl.

% Query to solve the problem
?- solve_problem.
