import time
from queue import PriorityQueue

from Maps.maps import Map,Parser


def uniform_cost(m: Map) -> list:
    print('UCS')
    start_time = time.time()

    visited = []
    visited_goals = []
    queue = PriorityQueue()
    queue.put((0, m.me))
    cost = 1
    while queue.queue:
        current = queue.get()
        children = m.get_successors(current[1][0], current[1][1])

        # Check it is visited goal or not
        if current in m.goals and current not in visited_goals:
            visited_goals.append(current)
            visited.clear()
            queue = PriorityQueue()
            queue.put((1, current))

        if len(visited_goals) == len(m.goals):
            break  # you can expand goal nodes too

        if current[1] not in visited:
            for i in children:
                if i not in visited:
                    queue.put((cost, i))

            visited.append(current[1])

    print('Uninformed Search')
    print('Duration:', time.time() - start_time)
    return visited

parser = Parser()
m = parser.get_map(1)
uniform_cost(m)
