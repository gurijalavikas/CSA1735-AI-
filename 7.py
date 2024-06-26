from collections import deque

def bfs(graph, start):
    # Keep track of visited nodes to avoid revisiting
    visited = set()
    # Use a queue to keep track of nodes to visit
    queue = deque([start])
    
    while queue:
        # Get the next node from the queue
        node = queue.popleft()
        
        # If this node hasn't been visited, process it
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

bfs(graph, 'A')
