import time
from Maps.maps import Map


def dfs(m: Map) -> list:
    start_time = time.time()

    visited = []
    visited_goals = []
    stack = [m.me]
    while stack:
        current = stack.pop()

        # Check current node is visited or not
        if current not in visited:
            visited.append(current)
        else:
            continue

        # Check it is visited goal or not
        if current in m.goals and current not in m.goals:
            visited_goals.append(current)

        if len(visited_goals) == len(m.goals):
            break  # you can expand goal nodes too

        for i in m.get_successors(current[0], current[1]):
            if i not in visited:
                stack.append(i)

    print('DFS Search')
    print('Duration:', time.time() - start_time)
    return visited
