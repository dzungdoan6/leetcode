from collections import deque

def bfs(graph, source):
    n = len(grid)
    stack = deque()
    visited = [False] * n
    stack.append(source)
    visited[source] = True

    # while deque is not empty
    while stack:
        vertex = stack.popleft()
        print(vertex)

        for i in range(n):
            if graph[vertex][i] == 1 and visited[i] is False:
                stack.append(i)
                visited[i] = True

def do_dfs(graph, v, visited):
    n = len(graph)
    visited.add(v)
    print(v)

    for i in range(n):
        if graph[v][i] == 1 and i not in visited:
            do_dfs(graph, i, visited)

def dfs(graph, source):
    visited = set()

    do_dfs(graph, source, visited)

grid = [[0,1,1,0,0],
        [1,0,1,1,0],
        [1,1,0,0,1],
        [0,1,0,0,1],
        [0,0,1,1,0]]

bfs(grid, 0)

grid2 = [[0,1,1,0],
         [0,0,1,0],
         [1,0,0,1],
         [0,0,0,1]]

print("\n")
dfs(grid2,2)