import time

from Maps.maps import Map


def bfs(m: Map) -> list:
    start_time = time.time()

    visited = []
    visited_goals = []
    queue = [m.me]
    while queue:
        current = queue.pop(0)

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
                queue.append(i)

    print('BFS Search')
    print('Duration:', time.time() - start_time)
    return visited
