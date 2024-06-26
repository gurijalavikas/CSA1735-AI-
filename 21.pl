% move(N, Source, Target, Auxiliary): Moves N disks from Source to Target using Auxiliary as helper.
move(0, _, _, _) :- !. % Base case: No move needed for 0 disks.
move(N, Source, Target, Auxiliary) :-
    N > 0,
    M is N - 1,
    move(M, Source, Auxiliary, Target), % Move M disks from Source to Auxiliary using Target as helper.
    format('Move disk ~w from ~w to ~w~n', [N, Source, Target]), % Move the Nth disk from Source to Target.
    move(M, Auxiliary, Target, Source). % Move M disks from Auxiliary to Target using Source as helper.
