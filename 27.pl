% Graph representation: edge(Node1, Node2, Cost).
edge(a, b, 1).
edge(a, c, 4).
edge(b, d, 2).
edge(b, e, 5).
edge(c, f, 3).
edge(d, g, 1).
edge(e, g, 2).
edge(f, g, 2).

% Heuristic values for each node (hypothetical values).
heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 5).
heuristic(d, 4).
heuristic(e, 3).
heuristic(f, 2).
heuristic(g, 0). % Goal node heuristic is 0.
